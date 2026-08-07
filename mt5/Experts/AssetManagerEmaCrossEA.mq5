#property strict
#property version   "1.00"
#property description "EMA crossover Expert using the fail-closed AssetManager MT5 gateway."
#property description "Add http://127.0.0.1:8282 to allowed WebRequest URLs."

#include <AssetManagerBridge.mqh>

input string GatewayUrl="http://127.0.0.1:8282";
input string GatewayToken="";
input string ExpertId="ema-cross-v1";
input int FastPeriod=12;
input int SlowPeriod=26;
input double VolumeLots=0.01;
input int StopLossPoints=250;
input int TakeProfitPoints=500;
input bool ExecuteSignals=false;
input bool ConfirmLive=false;

int fast_handle=INVALID_HANDLE;
int slow_handle=INVALID_HANDLE;
datetime last_bar_time=0;

int OnInit()
  {
   if(FastPeriod<=0 || SlowPeriod<=FastPeriod || VolumeLots<=0)
     {
      Print("Invalid EMA or volume parameters.");
      return INIT_PARAMETERS_INCORRECT;
     }
   if(GatewayToken=="")
     {
      Print("GatewayToken is required. The EA will not start without it.");
      return INIT_PARAMETERS_INCORRECT;
     }

   fast_handle=iMA(_Symbol,_Period,FastPeriod,0,MODE_EMA,PRICE_CLOSE);
   slow_handle=iMA(_Symbol,_Period,SlowPeriod,0,MODE_EMA,PRICE_CLOSE);
   if(fast_handle==INVALID_HANDLE || slow_handle==INVALID_HANDLE)
      return INIT_FAILED;

   PrintFormat("AssetManager EA ready. expert=%s execute=%s symbol=%s",
               ExpertId,ExecuteSignals ? "true" : "false",_Symbol);
   return INIT_SUCCEEDED;
  }

void OnDeinit(const int reason)
  {
   if(fast_handle!=INVALID_HANDLE)
      IndicatorRelease(fast_handle);
   if(slow_handle!=INVALID_HANDLE)
      IndicatorRelease(slow_handle);
  }

void OnTick()
  {
   datetime bar_time=iTime(_Symbol,_Period,0);
   if(bar_time==0 || bar_time==last_bar_time)
      return;
   last_bar_time=bar_time;

   double fast[2],slow[2];
   if(CopyBuffer(fast_handle,0,1,2,fast)!=2 ||
      CopyBuffer(slow_handle,0,1,2,slow)!=2)
      return;

   string side="";
   if(fast[0]<=slow[0] && fast[1]>slow[1])
      side="BUY";
   else if(fast[0]>=slow[0] && fast[1]<slow[1])
      side="SELL";
   else
      return;

   MqlTick tick;
   if(!SymbolInfoTick(_Symbol,tick))
      return;

   double price=(side=="BUY") ? tick.ask : tick.bid;
   double sl=(side=="BUY") ? price-StopLossPoints*_Point : price+StopLossPoints*_Point;
   double tp=(side=="BUY") ? price+TakeProfitPoints*_Point : price-TakeProfitPoints*_Point;
   int digits=(int)SymbolInfoInteger(_Symbol,SYMBOL_DIGITS);
   sl=NormalizeDouble(sl,digits);
   tp=NormalizeDouble(tp,digits);

   string signal_id=StringFormat("%s:%s:%I64d:%s",ExpertId,_Symbol,(long)bar_time,side);
   string response;
   bool accepted=AM_SendSignal(GatewayUrl,GatewayToken,ExpertId,signal_id,
                               _Symbol,side,VolumeLots,sl,tp,ExecuteSignals,
                               ConfirmLive,response);
   PrintFormat("AssetManager signal=%s accepted=%s response=%s",
               signal_id,accepted ? "true" : "false",response);
  }

void OnTradeTransaction(const MqlTradeTransaction &trans,
                        const MqlTradeRequest &request,
                        const MqlTradeResult &result)
  {
   if(trans.type==TRADE_TRANSACTION_REQUEST || trans.type==TRADE_TRANSACTION_DEAL_ADD)
      PrintFormat("AssetManager trade event type=%s order=%I64u deal=%I64u retcode=%u",
                  EnumToString(trans.type),trans.order,trans.deal,result.retcode);
  }
