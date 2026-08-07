#ifndef __ASSET_MANAGER_BRIDGE_MQH__
#define __ASSET_MANAGER_BRIDGE_MQH__

string AM_JsonEscape(string value)
  {
   StringReplace(value,"\\","\\\\");
   StringReplace(value,"\"","\\\"");
   StringReplace(value,"\r","\\r");
   StringReplace(value,"\n","\\n");
   return value;
  }

bool AM_PostJson(const string base_url,
                 const string path,
                 const string gateway_token,
                 const string json,
                 const int timeout_ms,
                 string &response)
  {
   char request_data[];
   char response_data[];
   string response_headers;
   string headers="Content-Type: application/json\r\n"
                  "X-MT5-Gateway-Token: "+gateway_token+"\r\n";

   int length=StringToCharArray(json,request_data,0,WHOLE_ARRAY,CP_UTF8);
   if(length>0)
      ArrayResize(request_data,length-1);

   ResetLastError();
   int http_code=WebRequest("POST",base_url+path,headers,timeout_ms,
                            request_data,response_data,response_headers);
   response=CharArrayToString(response_data,0,-1,CP_UTF8);

   if(http_code==-1)
     {
      PrintFormat("AssetManager WebRequest failed. error=%d",GetLastError());
      return false;
     }
   if(http_code<200 || http_code>=300)
     {
      PrintFormat("AssetManager gateway rejected request. http=%d body=%s",
                  http_code,response);
      return false;
     }
   return true;
  }

bool AM_SendSignal(const string base_url,
                   const string gateway_token,
                   const string expert_id,
                   const string signal_id,
                   const string symbol,
                   const string side,
                   const double volume,
                   const double stop_loss,
                   const double take_profit,
                   const bool execute,
                   const bool confirm_live,
                   string &response)
  {
   string json=StringFormat(
      "{\"signal_id\":\"%s\",\"expert_id\":\"%s\","
      "\"symbol\":\"%s\",\"side\":\"%s\",\"volume\":%.8f,"
      "\"observed_at_epoch\":%I64d,\"sl\":%.10f,\"tp\":%.10f,"
      "\"comment\":\"AssetManager EA\",\"execute\":%s,\"confirm_live\":%s}",
      AM_JsonEscape(signal_id),AM_JsonEscape(expert_id),AM_JsonEscape(symbol),
      AM_JsonEscape(side),volume,(long)TimeGMT(),stop_loss,take_profit,
      execute ? "true" : "false",confirm_live ? "true" : "false"
   );

   return AM_PostJson(base_url,"/api/v1/trading/mt5/experts/signals",
                      gateway_token,json,3000,response);
  }

#endif
