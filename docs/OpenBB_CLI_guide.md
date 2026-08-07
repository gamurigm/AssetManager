# Guía Completa de la CLI de OpenBB

Esta guía contiene todos los comandos disponibles (basados en las extensiones y proveedores instalados) junto con sus campos (flags/options).

## 🧪 Resultados de Pruebas Rápidas

Se han probado algunos comandos principales de forma automática:

- `/equity/price/quote`: Success
- `/equity/profile`: Success

*(Nota: Testear todos los cientos de comandos produciría bloqueos de API y excedería los límites de cuota, por lo que se prueban los endpoints más representativos).* 

---

## 📚 Todos los Comandos Disponibles

### Comando: `/commodity/price/spot`

**Descripción:** Commodity Spot Prices.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--commodity` (Opcional) `[Literal['wti', 'brent', 'natural_gas', 'jet_fuel', 'propane', 'heating_oil', 'diesel_gulf_coast', 'diesel_ny_harbor', 'diesel_la', 'gasoline_ny_harbor', 'gasoline_gulf_coast', 'rbob', 'all'] | None]`: Commodity name associated with the EIA spot price commodity data, default is 'all'.
  - `--frequency` (Opcional) `[Literal['a', 'q', 'm', 'w', 'd', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'] | None]`: Frequency aggregation to convert high frequency data to lower frequency.         None = No change         a = Annual         q = Quarterly         m = Monthly         w = Weekly         d = Daily         wef = Weekly, Ending Friday         weth = Weekly, Ending Thursday         wew = Weekly, Ending Wednesday         wetu = Weekly, Ending Tuesday         wem = Weekly, Ending Monday         wesu = Weekly, Ending Sunday         wesa = Weekly, Ending Saturday         bwew = Biweekly, Ending Wednesday         bwem = Biweekly, Ending Monday
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set.         avg = Average         sum = Sum         eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type         None = No transformation         chg = Change         ch1 = Change from Year Ago         pch = Percent Change         pc1 = Percent Change from Year Ago         pca = Compounded Annual Rate of Change         cch = Continuously Compounded Rate of Change         cca = Continuously Compounded Annual Rate of Change         log = Natural Log

---
### Comando: `/commodity/petroleum_status_report`

**Descripción:** EIA Weekly Petroleum Status Report.

- **Proveedores disponibles / soportados:** `eia`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `eia`:*
  - `--category` (Opcional) `[Literal['balance_sheet', 'inputs_and_production', 'refiner_blender_net_production', 'crude_petroleum_stocks', 'gasoline_fuel_stocks', 'total_gasoline_by_sub_padd', 'distillate_fuel_oil_stocks', 'imports', 'imports_by_country', 'weekly_estimates', 'spot_prices_crude_gas_heating', 'spot_prices_diesel_jet_fuel_propane', 'retail_prices'] | None]`: The group of data to be returned. The default is the balance sheet.
  - `--table` (Opcional) `[str | None]`: The specific table element within the category to be returned, default is 'stocks', if the category is 'weekly_estimates', else 'all'.     Note: Choices represent all available tables from the entire collection and are not all available for every category.     Invalid choices will raise a ValidationError with a message indicating the valid choices for the selected category.     Choices are:         all         conventional_gas         crude         crude_production         crude_production_avg         diesel         ethanol_plant_production         ethanol_plant_production_avg         exports         exports_avg         heating_oil         imports         imports_avg         imports_by_country         imports_by_country_avg         inputs_and_utilization         inputs_and_utilization_avg         jet_fuel         monthly         net_imports_inc_spr_avg         net_imports_incl_spr         net_production         net_production_avg         net_production_by_product         net_production_by_production_avg         product_by_region         product_by_region_avg         product_supplied         product_supplied_avg         propane         rbob         refiner_blender_net_production         refiner_blender_net_production_avg         stocks         supply         supply_avg         ulta_low_sulfur_distillate_reclassification         ulta_low_sulfur_distillate_reclassification_avg         weekly
  - `--use_cache` (Opcional) `[bool | None]`: Subsequent requests for the same source data are cached for the session using ALRU cache.

---
### Comando: `/commodity/short_term_energy_outlook`

**Descripción:** Monthly short term (18 month) projections using EIA's STEO model.

Source: www.eia.gov/steo/

- **Proveedores disponibles / soportados:** `eia`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `eia`:*
  - `--symbol` (Opcional) `[str | None]`: Symbol to get data for. If provided, overrides the 'table' parameter to return only the specified symbol from the STEO API.
  - `--table` (Opcional) `[Literal['01', '02', '03a', '03b', '03c', '03d', '03e', '04a', '04b', '04c', '04d', '05a', '05b', '06', '07a', '07b', '07c', '07d1', '07d2', '07e', '08', '09a', '09b', '09c', '10a', '10b'] | None]`: The specific table within the STEO dataset. Default is '01'. When 'symbol' is provided, this parameter is ignored.     01: US Energy Markets Summary     02: Nominal Energy Prices     03a: World Petroleum and Other Liquid Fuels Production, Consumption, and Inventories     03b: Non-OPEC Petroleum and Other Liquid Fuels Production     03c: World Petroleum and Other Liquid Fuels Production     03d: World Crude Oil Production     03e: World Petroleum and Other Liquid Fuels Consumption     04a: US Petroleum and Other Liquid Fuels Supply, Consumption, and Inventories     04b: US Hydrocarbon Gas Liquids (HGL) and Petroleum Refinery Balances     04c: US Regional Motor Gasoline Prices and Inventories     04d: US Biofuel Supply, Consumption, and Inventories     05a: US Natural Gas Supply, Consumption, and Inventories     05b: US Regional Natural Gas Prices     06: US Coal Supply, Consumption, and Inventories     07a: US Electricity Industry Overview     07b: US Regional Electricity Retail Sales     07c: US Regional Electricity Prices     07d1: US Regional Electricity Generation, Electric Power Sector     07d2: US Regional Electricity Generation, Electric Power Sector, continued     07e: US Electricity Generating Capacity     08: US Renewable Energy Consumption     09a: US Macroeconomic Indicators and CO2 Emissions     09b: US Regional Macroeconomic Data     09c: US Regional Weather Data     10a: Drilling Productivity Metrics     10b: Crude Oil and Natural Gas Production from Shale and Tight Formations
  - `--frequency` (Opcional) `[Literal['month', 'quarter', 'annual'] | None]`: The frequency of the data. Default is 'month'.

---
### Comando: `/commodity/psd_data`

**Descripción:** Get data tables and historical time series from the USDA FAS Production, Supply, and Distribution (PSD) Reports.

- **Proveedores disponibles / soportados:** `government_us`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `government_us`:*
  - `--report_id` (Opcional) `[str | None]`: Report ID to retrieve. Gets the current report for the given commodity and subject. These are predefined tables that are part of the PDF publication data. This parameter is ignored if 'commodity' is provided. Use the 'commodity' parameter for time series data. Valid reports are:     almonds_summary, almonds_supply_distribution, apples_selected_countries, apples_supply_distribution, barley_area_yield_production, barley_regional, barley_supply_disappearance, barley_world_production_consumption_stocks, barley_world_trade, beef_veal_production, beef_veal_trade, butter_production_consumption, butter_trade, cattle_stocks, cattle_trade, cheese_production_consumption, cheese_trade, cherries_selected_countries, cherries_supply_distribution, chicken_production, chicken_trade, china_grain_supply_demand, coarse_grains_area_yield_production, coarse_grains_regional, coarse_grains_world_production_consumption_stocks, coarse_grains_world_trade, coffee_arabica_production, coffee_consumption, coffee_ending_stocks, coffee_exports_green_bean, coffee_exports_soluble, coffee_exports_total, coffee_imports_green_bean, coffee_imports_soluble, coffee_imports_total, coffee_production, coffee_robusta_production, coffee_summary, coffee_summary_2, coffee_summary_3, coffee_summary_4, copra_palm_kernel_palm_oil_production, corn_area_yield_production, corn_barley_supply_demand, corn_regional, corn_supply_disappearance, corn_world_production_consumption_stocks, corn_world_trade, cotton_area_yield_production, cotton_area_yield_production_fcr, cotton_by_country, cotton_by_country_2, cotton_foreign_supply, cotton_monthly_changes, cotton_supply_distribution, cotton_supply_distribution_2, cotton_us_supply, cotton_world_supply, cotton_world_supply_use, cotton_world_supply_use_2, cottonseed_area_yield_production, eu_grain_supply_demand, grains_summary_comparison, grapefruit_selected_countries, grapes_selected_countries, grapes_supply_distribution, lemons_limes_selected_countries, milk_cow_numbers, milk_production_consumption, nonfat_dry_milk_production_consumption, nonfat_dry_milk_trade, oats_area_yield_production, oats_regional, oats_world_production_consumption_stocks, oats_world_trade, oilseeds_area_yield_production, oilseeds_china, oilseeds_eu, oilseeds_india, oilseeds_middle_east, oilseeds_products_world_supply_demand, oilseeds_southeast_asia, oilseeds_us_supply_distribution, oilseeds_world_commodity_view, oilseeds_world_country_view, orange_juice_supply_distribution, oranges_selected_countries, oranges_selected_countries_2, other_europe_grain_supply_demand, palm_coconut_fishmeal_world_supply_demand, palm_oil_world_supply, peaches_nectarines_selected_countries, peaches_nectarines_supply_distribution, peanut_area_yield_production, pears_selected_countries, pears_supply_distribution, pistachios_summary, pistachios_supply_distribution, pork_production, pork_trade, protein_meals_world_commodity_view, protein_meals_world_country_view, raisins_selected_countries, raisins_supply_distribution, rapeseed_area_yield_production, rapeseed_products_world_supply, rapeseed_products_world_supply_demand, rice_area_yield_production, rice_regional, rice_supply_demand, rice_world_production_consumption_stocks, rice_world_trade, russia_barley, russia_corn, russia_grain_supply_demand, russia_wheat, rye_area_yield_production, rye_regional, rye_world_production_consumption_stocks, rye_world_trade, sorghum_area_yield_production, sorghum_regional, sorghum_supply_disappearance, sorghum_world_production_consumption_stocks, sorghum_world_trade, soybean_meal_world_supply, soybean_oil_world_supply, soybeans_area_yield_production, soybeans_argentina_supply_distribution, soybeans_brazil_supply_distribution, soybeans_products_world_supply_demand, soybeans_products_world_trade, soybeans_us_supply_distribution, soybeans_world_supply, sugar_ending_stocks, sugar_imports_exports, sugar_production_consumption, sunflower_area_yield_production, sunflower_products_world_supply, sunflower_products_world_supply_demand, swine_stocks, swine_trade, tangerines_mandarins_selected_countries, us_grains_supply_distribution, vegetable_oils_minor_world_supply, vegetable_oils_world_commodity_view, vegetable_oils_world_country_view, walnuts_summary, walnuts_supply_distribution, wheat_area_yield_production, wheat_coarse_grains_supply_demand, wheat_coarse_grains_world_supply_demand, wheat_flour_products_world_trade, wheat_regional, wheat_supply_disappearance, wheat_world_production_consumption_stocks, whole_milk_powder_production_consumption, whole_milk_powder_trade, world_crop_production_summary
  - `--commodity` (Opcional) `[str | None]`: Commodity name to filter the data. If provided, retrieves time series data for the given commodity. Supplying both 'report_id' and 'commodity' will prioritize 'commodity' for time series data. Valid commodities are:     almonds, apples, barley, beef, broiler, butter, cattle, cheese, cherries, chicken, coffee, corn, cotton, dry_whole_milk_powder, fluid_milk, grapefruit, grapes, lemons_limes, meal_copra, meal_cottonseed, meal_fish, meal_palm_kernel, meal_peanut, meal_rapeseed, meal_soybean, meal_sunflowerseed, millet, mixed_grain, nonfat_dry_milk, oats, oil_coconut, oil_cottonseed, oil_olive, oil_palm, oil_palm_kernel, oil_peanut, oil_rapeseed, oil_soybean, oil_sunflowerseed, oilseed_copra, oilseed_cottonseed, oilseed_palm_kernel, oilseed_peanut, oilseed_rapeseed, oilseed_soybean, oilseed_sunflowerseed, orange_juice, oranges, peaches_nectarines, pears, pistachios, pork, rice, rye, sorghum, sugar, swine, tangerines_mandarins, walnuts, wheat
  - `--attribute` (Opcional) `[str | list[str] | None]`: Attribute to filter the data. If None, retrieves all available attributes for the commodity. Parameter is ignored when commodity is None. Valid attributes depend on the commodity, an invalid choice will show the available attributes for the entered commodity. All attributes choices are: annual_pct_change_per_cap_cons, arabica_production, area_harvested, area_planted, balance, bean_exports, bean_imports, bearing_trees, beef_cows_beg_stocks, beet_sugar_production, begin_stock_ctrl_app, begin_stock_other, beginning_stocks, calf_slaughter, cane_sugar_production, catch_for_reduction, commercial_production, consumption_change, cow_change, cow_slaughter, cows_in_milk, cows_milk_production, crush, cy_exp_to_us, cy_exports, cy_imp_from_us, cy_imports, dairy_cows_beg_stocks, deliv_to_processors, dom_consump_ctrl_app, dom_consump_other, dom_leaf_consumption, domestic_consumption, domestic_use, end_stocks_ctrl_app, end_stocks_other, ending_stocks, export_change, exportable_production, exports, exports_percent_production, extr_rate, factory_use_consum, farm_sales_weight_prod, feed_dom_consumption, feed_use_dom_consum, feed_waste_dom_cons, filter_production, fluid_use_dom_consum, food_use_dom_cons, for_processing, fresh_dom_consumption, fresh_dom_consumption_alt, fsi_consumption, human_consumption, human_dom_consumption, import_change, imports, imports_percent_consumption, industrial_dom_cons, intra_eu_exports, intra_eu_exports_alt, intra_eu_imports, inventory_balance, inventory_change, inventory_reference, loss, loss_and_residual, milling_rate, my_exp_to_eu, my_imp_from_eu, my_imp_from_us, non_bearing_trees, non_comm_production, non_filter_production, other_disappearance, other_exports, other_foreign_cons, other_imports, other_milk_production, other_production, other_slaughter, other_use_losses, per_capita_consumption, population, prod_from_table_grapes, prod_from_wine_grapes, production, production_change, production_to_cows, production_to_sows, raw_exports, raw_imports, refined_exp_raw_val, refined_imp_raw_val, roast_ground_exports, roast_ground_imports, robusta_production, rough_production, rst_ground_dom_consum, seed_to_lint_ratio, slaughter_reference, slaughter_to_inventory, slaughter_to_total_supply, sme, soluble_dom_cons, soluble_exports, soluble_imports, sow_beginning_stocks, sow_change, sow_slaughter, stocks_to_use, stocks_to_use_months, total_disappearance, total_disappearance_alt, total_distribution, total_grape_crush, total_slaughter, total_supply, total_trees, total_use, total_utilization, ty_exports, ty_imp_from_us, ty_imports, us_leaf_dom_cons, us_leaf_imports, utilization_for_alcohol, utilization_for_sugar, weights, withdrawal_from_market, yield
  - `--country` (Opcional) `[str | list[str] | None]`: Country code(s) to filter the data. If None, retrieves data for all countries. Parameter is ignored when commodity is None. Valid country codes include: afghanistan, albania, algeria, angola, argentina, armenia, australia, austria, azerbaijan, bahamas, bahrain, bangladesh, barbados, belarus, belgium, belize, benin, bhutan, bolivia, bosnia_and_herzegovina, botswana, brazil, brunei, bulgaria, burkina_faso, burma, burundi, cabo_verde, cambodia, cameroon, canada, caribbean, central_african_republic, central_america, chad, chile, china, colombia, comoros, congo_brazzaville, congo_kinshasa, costa_rica, cote_divoire, croatia, cuba, cyprus, czech_republic, czechia, denmark, djibouti, dominica, dominican_republic, east_asia, ecuador, egypt, el_salvador, equatorial_guinea, eritrea, estonia, eswatini, ethiopia, eu, eu_15, eu_25, european_union, fiji, finland, former_soviet_union, france, gabon, gambia, georgia, germany, ghana, greece, guatemala, guinea, guinea_bissau, guyana, haiti, honduras, hong_kong, hungary, iceland, india, indonesia, iran, iraq, ireland, israel, italy, ivory_coast, jamaica, japan, jordan, kazakhstan, kenya, kosovo, kuwait, kyrgyzstan, laos, latvia, lebanon, lesotho, liberia, libya, lithuania, luxembourg, macau, macedonia, madagascar, malawi, malaysia, maldives, mali, malta, mauritania, mauritius, mexico, middle_east, moldova, mongolia, montenegro, morocco, mozambique, myanmar, namibia, nepal, netherlands, new_caledonia, new_zealand, nicaragua, niger, nigeria, north_africa, north_america, north_korea, north_macedonia, norway, oceania, oman, other_europe, pakistan, panama, papua_new_guinea, paraguay, peru, philippines, poland, portugal, puerto_rico, qatar, reunion, romania, russia, rwanda, samoa, sao_tome_and_principe, saudi_arabia, senegal, serbia, seychelles, sierra_leone, singapore, slovakia, slovenia, solomon_islands, somalia, south_africa, south_america, south_asia, south_korea, south_sudan, southeast_asia, spain, sri_lanka, sub_saharan_africa, sudan, suriname, swaziland, sweden, switzerland, syria, taiwan, tajikistan, tanzania, thailand, togo, tonga, trinidad_and_tobago, tunisia, turkey, turkmenistan, uganda, ukraine, united_arab_emirates, united_kingdom, united_states, uruguay, uzbekistan, vanuatu, venezuela, vietnam, world, yemen, zambia, zimbabwe
  - `--aggregate_regions` (Opcional) `[bool | None]`: Whether to include regional and world aggregates in the data. Parameter is ignored when 'commodity' is None.
  - `--start_year` (Opcional) `[int | None]`: Start year for filtering time series data. None returns from the beginning of the series. Parameter is ignored when 'commodity' is None.
  - `--end_year` (Opcional) `[int | None]`: End year for filtering time series data. If None, returns up to the most recent year. Parameter is ignored when 'commodity' is None.

---
### Comando: `/commodity/psd_report`

**Descripción:** Agriculture commodity production, supply, and distribution PDF reports (World Agricultural Outlook).

This command returns only the results portion of the OBBject response.
It contains a dictionary where the PDF content is base64 encoded under the 'content' key.

- **Proveedores disponibles / soportados:** `government_us`

**Flags / Parámetros (Standard & Providers):**
  - `--commodity` *(Requerido)* `[str]`: Commodity for the report.
  - `--year` *(Requerido)* `[int]`: Year of the report.
  - `--month` *(Requerido)* `[int]`: Month of the report.

  *Exclusivos del proveedor `government_us`:*

---
### Comando: `/commodity/weather_bulletins`

**Descripción:** Get current and historical weather bulletins with their PDF links.

This command returns only the results portion of the OBBject response.
It contains a list of dictionaries where each dictionary has 'label' and 'value' keys.

Use this endpoint to programmatically access the list of available weather bulletins.
Suitable for dropdown selections in a UI.

- **Proveedores disponibles / soportados:** `government_us`

**Flags / Parámetros (Standard & Providers):**
  - `--year` (Opcional) `[int | None]`: Year of the data. Default is the current year.
  - `--month` (Opcional) `[int | None]`: Month of the data. If not provided, data for the entire year is returned.
  - `--week` (Opcional) `[int | None]`: Numeric week of the data, relative to the month. If not provided, data for the entire month is returned.

  *Exclusivos del proveedor `government_us`:*

---
### Comando: `/commodity/weather_bulletins_download`

**Descripción:** Download one, or more, weather bulletin documents.

This command returns only the results portion of the OBBject response.
It contains a list of dictionaries where the base64 encoded content of the document is under the 'content' key.

- **Proveedores disponibles / soportados:** `government_us`

**Flags / Parámetros (Standard & Providers):**
  - `--urls` *(Requerido)* `[str | dict | list | list[str | dict | list]]`: URLs for reports to download. Multiple items allowed for provider(s): government_us.

  *Exclusivos del proveedor `government_us`:*

---
### Comando: `/crypto/price/historical`

**Descripción:** Get historical price data for cryptocurrency pair(s) within a provider.

- **Proveedores disponibles / soportados:** `fmp, polygon, tiingo, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp, polygon, tiingo, yfinance.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fmp`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '1h', '1d'] | None]`: Time interval of the data to return.

  *Exclusivos del proveedor `polygon`:*
  - `--interval` (Opcional) `[str | None]`: Time interval of the data to return. The numeric portion of the interval can be any positive integer. The letter portion can be one of the following: s, m, h, d, W, M, Q, Y
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order of the data. This impacts the results in combination with the 'limit' parameter. The results are always returned in ascending order by date.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `tiingo`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '15m', '30m', '90m', '1h', '2h', '4h', '1d', '7d', '30d'] | None]`: Time interval of the data to return.
  - `--exchanges` (Opcional) `[list[str] | str | None]`: To limit the query to a subset of exchanges e.g. ['POLONIEX', 'GDAX']

  *Exclusivos del proveedor `yfinance`:*
  - `--interval` (Opcional) `[Literal['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1W', '1M', '1Q'] | None]`: Time interval of the data to return.

---
### Comando: `/crypto/search`

**Descripción:** Search available cryptocurrency pairs within a provider.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--query` (Opcional) `[str | None]`: Search query.

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/currency/price/historical`

**Descripción:** Currency Historical Price. Currency historical data.

Currency historical prices refer to the past exchange rates of one currency against
another over a specific period.
This data provides insight into the fluctuations and trends in the foreign exchange market,
helping analysts, traders, and economists understand currency performance,
evaluate economic health, and make predictions about future movements.

- **Proveedores disponibles / soportados:** `fmp, polygon, tiingo, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Can use CURR1-CURR2 or CURR1CURR2 format. Multiple items allowed for provider(s): fmp, polygon, tiingo, yfinance.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fmp`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '1h', '1d'] | None]`: Time interval of the data to return.

  *Exclusivos del proveedor `polygon`:*
  - `--interval` (Opcional) `[str | None]`: Time interval of the data to return. The numeric portion of the interval can be any positive integer. The letter portion can be one of the following: s, m, h, d, W, M, Q, Y
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order of the data. This impacts the results in combination with the 'limit' parameter. The results are always returned in ascending order by date.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `tiingo`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '15m', '30m', '90m', '1h', '2h', '4h', '1d', '5d', '21d'] | None]`: Time interval of the data to return.

  *Exclusivos del proveedor `yfinance`:*
  - `--interval` (Opcional) `[Literal['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1W', '1M', '1Q'] | None]`: Time interval of the data to return.

---
### Comando: `/currency/search`

**Descripción:** Currency Search.

Search available currency pairs.
Currency pairs are the national currencies from two countries coupled for trading on
the foreign exchange (FX) marketplace.
Both currencies will have exchange rates on which the trade will have its position basis.
All trading within the forex market, whether selling, buying, or trading, will take place through currency pairs.
(ref: Investopedia)
Major currency pairs include pairs such as EUR/USD, USD/JPY, GBP/USD, etc.

- **Proveedores disponibles / soportados:** `fmp, intrinio, polygon`

**Flags / Parámetros (Standard & Providers):**
  - `--query` (Opcional) `[str | None]`: Query to search for currency pairs.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `intrinio`:*

  *Exclusivos del proveedor `polygon`:*

---
### Comando: `/currency/reference_rates`

**Descripción:** Get current, official, currency reference rates.

Foreign exchange reference rates are the exchange rates set by a major financial institution or regulatory body,
serving as a benchmark for the value of currencies around the world.
These rates are used as a standard to facilitate international trade and financial transactions,
ensuring consistency and reliability in currency conversion.
They are typically updated on a daily basis and reflect the market conditions at a specific time.
Central banks and financial institutions often use these rates to guide their own exchange rates,
impacting global trade, loans, and investments.

- **Proveedores disponibles / soportados:** `ecb`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `ecb`:*

---
### Comando: `/currency/snapshots`

**Descripción:** Snapshots of currency exchange rates from an indirect or direct perspective of a base currency.

- **Proveedores disponibles / soportados:** `fmp, polygon`

**Flags / Parámetros (Standard & Providers):**
  - `--base` (Opcional) `[str | None | list[str | None]]`: The base currency symbol. Multiple items allowed for provider(s): fmp, polygon.
  - `--quote_type` (Opcional) `[Literal['direct', 'indirect'] | None]`: Whether the quote is direct or indirect. Selecting 'direct' will return the exchange rate as the amount of domestic currency required to buy one unit of the foreign currency. Selecting 'indirect' (default) will return the exchange rate as the amount of foreign currency required to buy one unit of the domestic currency.
  - `--counter_currencies` (Opcional) `[str | list[str] | None]`: An optional list of counter currency symbols to filter for. None returns all.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `polygon`:*

---
### Comando: `/derivatives/options/chains`

**Descripción:** Get the complete options chain for a ticker.

- **Proveedores disponibles / soportados:** `cboe, deribit, intrinio, tmx, tradier, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `cboe`:*
  - `--use_cache` (Opcional) `[bool | None]`: When True, the company directories will be cached for24 hours and are used to validate symbols. The results of the function are not cached. Set as False to bypass.

  *Exclusivos del proveedor `deribit`:*

  *Exclusivos del proveedor `intrinio`:*
  - `--delay` (Opcional) `[Literal['eod', 'realtime', 'delayed'] | None]`: Whether to return delayed, realtime, or eod data.
  - `--date` (Opcional) `[date | None | str]`: The end-of-day date for options chains data.
  - `--option_type` (Opcional) `[Literal['call', 'put'] | None]`: The option type, call or put, 'None' is both (default).
  - `--moneyness` (Opcional) `[Literal['otm', 'itm', 'all'] | None]`: Return only contracts that are in or out of the money, default is 'all'. Parameter is ignored when a date is supplied.
  - `--strike_gt` (Opcional) `[int | None]`: Return options with a strike price greater than the given value. Parameter is ignored when a date is supplied.
  - `--strike_lt` (Opcional) `[int | None]`: Return options with a strike price less than the given value. Parameter is ignored when a date is supplied.
  - `--volume_gt` (Opcional) `[int | None]`: Return options with a volume greater than the given value. Parameter is ignored when a date is supplied.
  - `--volume_lt` (Opcional) `[int | None]`: Return options with a volume less than the given value. Parameter is ignored when a date is supplied.
  - `--oi_gt` (Opcional) `[int | None]`: Return options with an open interest greater than the given value. Parameter is ignored when a date is supplied.
  - `--oi_lt` (Opcional) `[int | None]`: Return options with an open interest less than the given value. Parameter is ignored when a date is supplied.
  - `--model` (Opcional) `[Literal['black_scholes', 'bjerk'] | None]`: The pricing model to use for options chains data, default is 'black_scholes'. Parameter is ignored when a date is supplied.
  - `--show_extended_price` (Opcional) `[bool | None]`: Whether to include OHLC type fields, default is True. Parameter is ignored when a date is supplied.
  - `--include_related_symbols` (Opcional) `[bool | None]`: Include related symbols that end in a 1 or 2 because of a corporate action, default is False.

  *Exclusivos del proveedor `tmx`:*
  - `--date` (Opcional) `[date | None | str]`: A specific date to get data for.
  - `--use_cache` (Opcional) `[bool | None]`: Caching is used to validate the supplied ticker symbol, or if a historical EOD chain is requested. To bypass, set to False.

  *Exclusivos del proveedor `tradier`:*

  *Exclusivos del proveedor `yfinance`:*

---
### Comando: `/derivatives/options/surface`

**Descripción:** Filter and process the options chains data for volatility.

Data posted can be an instance of OptionsChainsData,
a pandas DataFrame, or a list of dictionaries.
Data should contain the fields:

- `expiration`: The expiration date of the option.
- `strike`: The strike price of the option.
- `option_type`: The type of the option (call or put).
- `implied_volatility`: The implied volatility of the option. Or 'target' field.
- `open_interest`: The open interest of the option.
- `volume`: The trading volume of the option.
- `dte` : Optional, days to expiration (DTE) of the option.
- `underlying_price`: Optional, the price of the underlying asset.

Results from the `/derivatives/options/chains` endpoint are the preferred input.

If `underlying_price` is not supplied in the data as a field, it must be provided as a parameter.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[Data | ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` (Opcional) `[str]`: 
  - `--underlying_price` (Opcional) `[float | None]`: 
  - `--option_type` (Opcional) `[None]`: 
  - `--dte_min` (Opcional) `[int | None]`: 
  - `--dte_max` (Opcional) `[int | None]`: 
  - `--moneyness` (Opcional) `[float | None]`: 
  - `--strike_min` (Opcional) `[float | None]`: 
  - `--strike_max` (Opcional) `[float | None]`: 
  - `--oi` (Opcional) `[bool]`: 
  - `--volume` (Opcional) `[bool]`: 
  - `--theme` (Opcional) `[Literal['dark', 'light']]`: 
  - `--chart_params` (Opcional) `[dict | None]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/derivatives/options/unusual`

**Descripción:** Get the complete options chain for a ticker.

- **Proveedores disponibles / soportados:** `intrinio`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None]`: Symbol to get data for. (the underlying symbol)

  *Exclusivos del proveedor `intrinio`:*
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format. If no symbol is supplied, requests are only allowed for a single date. Use the start_date for the target date. Intrinio appears to have data beginning Feb/2022, but is unclear when it actually began.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format. If a symbol is not supplied, do not include an end date.
  - `--trade_type` (Opcional) `[Literal['block', 'sweep', 'large'] | None]`: The type of unusual activity to query for.
  - `--sentiment` (Opcional) `[Literal['bullish', 'bearish', 'neutral'] | None]`: The sentiment type to query for.
  - `--min_value` (Opcional) `[int | float | None]`: The inclusive minimum total value for the unusual activity.
  - `--max_value` (Opcional) `[int | float | None]`: The inclusive maximum total value for the unusual activity.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return. A typical day for all symbols will yield 50-80K records. The API will paginate at 1000 records. The high default limit (100K) is to be able to reliably capture the most days. The high absolute limit (1.25M) is to allow for outlier days. Queries at the absolute limit will take a long time, and might be unreliable. Apply filters to improve performance.
  - `--source` (Opcional) `[Literal['delayed', 'realtime'] | None]`: The source of the data. Either realtime or delayed.

---
### Comando: `/derivatives/options/snapshots`

**Descripción:** Get a snapshot of the options market universe.

- **Proveedores disponibles / soportados:** `intrinio`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `intrinio`:*
  - `--date` (Opcional) `[date | datetime | str | None | str]`: The date of the data. Can be a datetime or an ISO datetime string. Data appears to go back to around 2022-06-01 Example: '2024-03-08T12:15:00+0400'
  - `--only_traded` (Opcional) `[bool | None]`: Only include options that have been traded during the session, default is True. Setting to false will dramatically increase the size of the response - use with caution.

---
### Comando: `/derivatives/futures/historical`

**Descripción:** Historical futures prices.

- **Proveedores disponibles / soportados:** `deribit, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): deribit, yfinance.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--expiration` (Opcional) `[str | None]`: Future expiry date with format YYYY-MM

  *Exclusivos del proveedor `deribit`:*
  - `--interval` (Opcional) `[Literal['1m', '3m', '5m', '10m', '15m', '30m', '1h', '2h', '3h', '6h', '12h', '1d'] | None]`: Time interval of the data to return.

  *Exclusivos del proveedor `yfinance`:*
  - `--interval` (Opcional) `[Literal['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1W', '1M', '1Q'] | None]`: Time interval of the data to return.

---
### Comando: `/derivatives/futures/curve`

**Descripción:** Futures Term Structure, current or historical.

- **Proveedores disponibles / soportados:** `cboe, deribit, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--date` (Opcional) `[date | str | None | list[date | str | None]]`: A specific date to get data for. Multiple items allowed for provider(s): cboe, yfinance.

  *Exclusivos del proveedor `cboe`:*
  - `--symbol` (Opcional) `[Literal['VX_AM', 'VX_EOD'] | None]`: Symbol to get data for.Default is 'VX_EOD'. Entered dates return the data nearest to the entered date.     'VX_AM' = Mid-Morning TWAP Levels     'VX_EOD' = 4PM Eastern Time Levels

  *Exclusivos del proveedor `deribit`:*
  - `--symbol` (Opcional) `[Literal['BTC', 'ETH', 'PAXG'] | None]`: Symbol to get data for. Default is 'btc' Supported symbols are: ['btc', 'eth', 'paxg']
  - `--hours_ago` (Opcional) `[int | list[int] | str | None]`: Compare the current curve with the specified number of hours ago. Default is None.

  *Exclusivos del proveedor `yfinance`:*

---
### Comando: `/derivatives/futures/instruments`

**Descripción:** Get reference data for available futures instruments by provider.

- **Proveedores disponibles / soportados:** `deribit`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `deribit`:*

---
### Comando: `/derivatives/futures/info`

**Descripción:** Get current trading statistics by futures contract symbol.

- **Proveedores disponibles / soportados:** `deribit`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `deribit`:*
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for. Perpetual contracts can be referenced by their currency pair - i.e, SOLUSDC - or by their official Deribit symbol - i.e, SOL_USDC-PERPETUAL For a list of currently available instruments, use `derivatives.futures.instruments()`

---
### Comando: `/econometrics/correlation_matrix`

**Descripción:** Get the correlation matrix of an input dataset.

The correlation matrix provides a view of how different variables in your dataset relate to one another.
By quantifying the degree to which variables move in relation to each other, this matrix can help identify patterns,
trends, and potential areas for deeper analysis. The correlation score ranges from -1 to 1, with -1 indicating a
perfect negative correlation, 0 indicating no correlation, and 1 indicating a perfect positive correlation.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--method` (Opcional) `[Literal['pearson', 'kendall', 'spearman']]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/econometrics/ols_regression`

**Descripción:** Perform Ordinary Least Squares (OLS) regression.

OLS regression is a fundamental statistical method to explore and model the relationship between a
dependent variable and one or more independent variables. By fitting the best possible linear equation to the data,
it helps uncover how changes in the independent variables are associated with changes in the dependent variable.
This returns the model and results objects from statsmodels library.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--y_column` *(Requerido)* `[str]`: 
  - `--x_columns` *(Requerido)* `[list[str]]`: 

---
### Comando: `/econometrics/ols_regression_summary`

**Descripción:** Perform Ordinary Least Squares (OLS) regression.

This returns the summary object from statsmodels.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--y_column` *(Requerido)* `[str]`: 
  - `--x_columns` *(Requerido)* `[list[str]]`: 

---
### Comando: `/econometrics/autocorrelation`

**Descripción:** Perform Durbin-Watson test for autocorrelation.

The Durbin-Watson test is a widely used method for detecting the presence of autocorrelation in the residuals
from a statistical or econometric model. Autocorrelation occurs when past values in the data series influence
future values, which can be a critical issue in time-series analysis, affecting the reliability of
model predictions. The test provides a statistic that ranges from 0 to 4, where a value around 2 suggests
no autocorrelation, values towards 0 indicate positive autocorrelation, and values towards 4 suggest
negative autocorrelation. Understanding the degree of autocorrelation helps in refining models to better capture
the underlying dynamics of the data, ensuring more accurate and trustworthy results.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--y_column` *(Requerido)* `[str]`: 
  - `--x_columns` *(Requerido)* `[list[str]]`: 

---
### Comando: `/econometrics/residual_autocorrelation`

**Descripción:** Perform Breusch-Godfrey Lagrange Multiplier tests for residual autocorrelation.

The Breusch-Godfrey Lagrange Multiplier test is a sophisticated tool for uncovering autocorrelation within the
residuals of a regression model. Autocorrelation in residuals can indicate that a model fails to capture some
aspect of the underlying data structure, possibly leading to biased or inefficient estimates.
By specifying the number of lags, you can control the depth of the test to check for autocorrelation,
allowing for a tailored analysis that matches the specific characteristics of your data.
This test is particularly valuable in econometrics and time-series analysis, where understanding the independence
of errors is crucial for model validity.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--y_column` *(Requerido)* `[str]`: 
  - `--x_columns` *(Requerido)* `[list[str]]`: 
  - `--lags` (Opcional) `[int]`: 

---
### Comando: `/econometrics/cointegration`

**Descripción:** Show co-integration between two timeseries using the two step Engle-Granger test.

The two-step Engle-Granger test is a method designed to detect co-integration between two time series.
Co-integration is a statistical property indicating that two or more time series move together over the long term,
even if they are individually non-stationary. This concept is crucial in economics and finance, where identifying
pairs or groups of assets that share a common stochastic trend can inform long-term investment strategies
and risk management practices. The Engle-Granger test first checks for a stable, long-term relationship by
regressing one time series on the other and then tests the residuals for stationarity.
If the residuals are found to be stationary, it suggests that despite any short-term deviations,
the series are bound by an equilibrium relationship over time.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--columns` *(Requerido)* `[list[str]]`: 

---
### Comando: `/econometrics/causality`

**Descripción:** Perform Granger causality test to determine if X 'causes' y.

The Granger causality test is a statistical hypothesis test to determine if one time series is useful in
forecasting another. While 'causality' in this context does not imply a cause-and-effect relationship in
the philosophical sense, it does test whether changes in one variable are systematically followed by changes
in another variable, suggesting a predictive relationship. By specifying a lag, you set the number of periods to
look back in the time series to assess this relationship. This test is particularly useful in economic and
financial data analysis, where understanding the lead-lag relationship between indicators can inform investment
decisions and policy making.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--y_column` *(Requerido)* `[str]`: 
  - `--x_column` *(Requerido)* `[str]`: 
  - `--lag` (Opcional) `[int]`: 

---
### Comando: `/econometrics/unit_root`

**Descripción:** Perform Augmented Dickey-Fuller (ADF) unit root test.

The ADF test is a popular method for testing the presence of a unit root in a time series.
A unit root indicates that the series may be non-stationary, meaning its statistical properties such as mean,
variance, and autocorrelation can change over time. The presence of a unit root suggests that the time series might
be influenced by a random walk process, making it unpredictable and challenging for modeling and forecasting.
The 'regression' parameter allows you to specify the model used in the test: 'c' for a constant term,
'ct' for a constant and trend term, and 'ctt' for a constant, linear, and quadratic trend.
This flexibility helps tailor the test to the specific characteristics of your data, providing a more accurate
assessment of its stationarity.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--column` *(Requerido)* `[str]`: 
  - `--regression` (Opcional) `[Literal['c', 'ct', 'ctt']]`: 

---
### Comando: `/econometrics/panel_random_effects`

**Descripción:** Perform One-way Random Effects model for panel data.

One-way Random Effects model to panel data is offering a nuanced approach to analyzing data that spans across both
time and entities (such as individuals, companies, countries, etc.). By acknowledging and modeling the random
variation that exists within these entities, this method provides insights into the general patterns that
emerge across the dataset.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--y_column` *(Requerido)* `[str]`: 
  - `--x_columns` *(Requerido)* `[list[str]]`: 

---
### Comando: `/econometrics/panel_between`

**Descripción:** Perform a Between estimator regression on panel data.

The Between estimator for regression analysis on panel data is focusing on the differences between entities
(such as individuals, companies, or countries) over time. By aggregating the data for each entity and analyzing the
average outcomes, this method provides insights into the overall impact of explanatory variables (x_columns) on
the dependent variable (y_column) across all entities.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--y_column` *(Requerido)* `[str]`: 
  - `--x_columns` *(Requerido)* `[list[str]]`: 

---
### Comando: `/econometrics/panel_pooled`

**Descripción:** Perform a Pooled coefficient estimator regression on panel data.

The Pooled coefficient estimator for regression analysis on panel data is treating the data as a large
cross-section without distinguishing between variations across time or entities
(such as individuals, companies, or countries). By assuming that the explanatory variables (x_columns) have a
uniform effect on the dependent variable (y_column) across all entities and time periods, this method simplifies
the analysis and provides a generalized view of the relationships within the data.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--y_column` *(Requerido)* `[str]`: 
  - `--x_columns` *(Requerido)* `[list[str]]`: 

---
### Comando: `/econometrics/panel_fixed`

**Descripción:** One- and two-way fixed effects estimator for panel data.

The Fixed Effects estimator to panel data is enabling a focused analysis on the unique characteristics of entities
(such as individuals, companies, or countries) and/or time periods. By controlling for entity-specific and/or
time-specific influences, this method isolates the effect of explanatory variables (x_columns) on the dependent
variable (y_column), under the assumption that these entity or time effects capture unobserved heterogeneity.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--y_column` *(Requerido)* `[str]`: 
  - `--x_columns` *(Requerido)* `[list[str]]`: 

---
### Comando: `/econometrics/panel_first_difference`

**Descripción:** Perform a first-difference estimate for panel data.

The First-Difference estimator for panel data analysis is focusing on the changes between consecutive observations
for each entity (such as individuals, companies, or countries). By differencing the data, this method effectively
removes entity-specific effects that are constant over time, allowing for the examination of the impact of changes
in explanatory variables (x_columns) on the change in the dependent variable (y_column).

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--y_column` *(Requerido)* `[str]`: 
  - `--x_columns` *(Requerido)* `[list[str]]`: 

---
### Comando: `/econometrics/panel_fmac`

**Descripción:** Fama-MacBeth estimator for panel data.

The Fama-MacBeth estimator, a two-step procedure renowned for its application in finance to estimate the risk
premiums and evaluate the capital asset pricing model. By first estimating cross-sectional regressions for each
time period and then averaging the regression coefficients over time, this method provides insights into the
relationship between the dependent variable (y_column) and explanatory variables (x_columns) across different
entities (such as individuals, companies, or countries).

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--y_column` *(Requerido)* `[str]`: 
  - `--x_columns` *(Requerido)* `[list[str]]`: 

---
### Comando: `/econometrics/variance_inflation_factor`

**Descripción:** Calculate VIF (variance inflation factor), which tests for collinearity.

It quantifies the severity of multicollinearity in an ordinary least squares regression analysis. The square
root of the variance inflation factor indicates how much larger the standard error increases compared to if
that variable had 0 correlation to other predictor variables in the model.

It is defined as:

$ VIF_i = 1 / (1 - R_i^2) $
where $ R_i $ is the coefficient of determination of the regression equation with the column i being the result
from the i:th series being the exogenous variable.

A VIF over 5 indicates a high collinearity and correlation. Values over 10 indicates causes problems, while a
value of 1 indicates no correlation. Thus VIF values between 1 and 5 are most commonly considered acceptable.
In order to improve the results one can often remove a column with high VIF.

For further information see: https://en.wikipedia.org/wiki/Variance_inflation_factor

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--columns` (Opcional) `[list[str] | None]`: 

---
### Comando: `/economy/gdp/forecast`

**Descripción:** Get Forecasted GDP Data.

- **Proveedores disponibles / soportados:** `oecd`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `oecd`:*
  - `--country` (Opcional) `[str | None]`: Country, or countries, to get forward GDP projections for. Default is all.
  - `--frequency` (Opcional) `[Literal['annual', 'quarter'] | None]`: Frequency of the data, default is annual.
  - `--units` (Opcional) `[Literal['current_prices', 'volume', 'capita', 'growth', 'deflator'] | None]`: Units of the data, default is volume (chain linked volume, 2015). 'current_prices', 'volume', and 'capita' are expressed in USD; 'growth' as a percent; 'deflator' as an index.

---
### Comando: `/economy/gdp/nominal`

**Descripción:** Get Nominal GDP Data.

- **Proveedores disponibles / soportados:** `econdb, oecd`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `econdb`:*
  - `--country` (Opcional) `[str | None]`: The country to get data.Use 'all' to get data for all available countries.
  - `--use_cache` (Opcional) `[bool | None]`: If True, the request will be cached for one day. Using cache is recommended to avoid needlessly requesting the same data.

  *Exclusivos del proveedor `oecd`:*
  - `--country` (Opcional) `[str | None]`: The country to get data. Use 'all' to get data for all available countries.
  - `--frequency` (Opcional) `[Literal['quarter', 'annual'] | None]`: Frequency of the data.
  - `--units` (Opcional) `[Literal['level', 'index', 'capita'] | None]`: The unit of measurement for the data.Both 'level' and 'capita' (per) are measured in USD.
  - `--price_base` (Opcional) `[Literal['current_prices', 'volume'] | None]`: Price base for the data, volume is chain linked volume.

---
### Comando: `/economy/gdp/real`

**Descripción:** Get Real GDP Data.

- **Proveedores disponibles / soportados:** `econdb, oecd`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `econdb`:*
  - `--country` (Opcional) `[str | None]`: The country to get data.Use 'all' to get data for all available countries.
  - `--use_cache` (Opcional) `[bool | None]`: If True, the request will be cached for one day. Using cache is recommended to avoid needlessly requesting the same data.

  *Exclusivos del proveedor `oecd`:*
  - `--country` (Opcional) `[str | None]`: The country to get data. Use 'all' to get data for all available countries.
  - `--frequency` (Opcional) `[Literal['quarter', 'annual'] | None]`: Frequency of the data.

---
### Comando: `/economy/shipping/port_info`

**Descripción:** Get general metadata and statistics for all ports from a given provider.

- **Proveedores disponibles / soportados:** `imf`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `imf`:*
  - `--continent` (Opcional) `[Literal['north_america', 'europe', 'asia_pacific', 'south_america', 'africa'] | None]`: Filter by continent. This parameter is ignored when a `country` is provided.
  - `--country` (Opcional) `[Literal['ABW', 'AGO', 'AIA', 'ALB', 'ARE', 'ARG', 'ASM', 'ATG', 'AUS', 'AZE', 'BEL', 'BEN', 'BES', 'BGD', 'BGR', 'BHR', 'BHS', 'BLM', 'BLZ', 'BRA', 'BRB', 'BRN', 'CAN', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COK', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CUW', 'CYM', 'CYP', 'DEU', 'DJI', 'DMA', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESP', 'EST', 'FIN', 'FJI', 'FRA', 'FRO', 'FSM', 'GAB', 'GBR', 'GEO', 'GHA', 'GIB', 'GIN', 'GLP', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD', 'GTM', 'GUF', 'GUM', 'GUY', 'HKG', 'HND', 'HRV', 'HTI', 'IDN', 'IND', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LBN', 'LBR', 'LBY', 'LCA', 'LKA', 'LTU', 'LVA', 'MAC', 'MAF', 'MAR', 'MDA', 'MDG', 'MDV', 'MEX', 'MHL', 'MLT', 'MMR', 'MNE', 'MNP', 'MOZ', 'MRT', 'MSR', 'MTQ', 'MUS', 'MYS', 'MYT', 'NAM', 'NCL', 'NGA', 'NIC', 'NLD', 'NOR', 'NRU', 'NZL', 'OMN', 'PAK', 'PAN', 'PER', 'PHL', 'PLW', 'PNG', 'POL', 'PRI', 'PRT', 'PYF', 'QAT', 'REU', 'ROU', 'RUS', 'SAU', 'SDN', 'SEN', 'SGP', 'SLB', 'SLE', 'SLV', 'SOM', 'STP', 'SUR', 'SVN', 'SWE', 'SXM', 'SYC', 'SYR', 'TCA', 'TGO', 'THA', 'TKM', 'TLS', 'TON', 'TTO', 'TUN', 'TUR', 'TUV', 'TWN', 'TZA', 'UKR', 'URY', 'USA', 'VCT', 'VEN', 'VGB', 'VIR', 'VNM', 'VUT', 'WSM', 'YEM', 'ZAF'] | None]`: Country to focus on. Enter as a 3-letter ISO country code. This parameter supersedes `continent` if both are provided.
  - `--port_code` (Opcional) `[str | None]`: This is a dummy parameter to allow grouping in OpenBB Workspace widgets.
  - `--limit` (Opcional) `[int | None]`: Limit the number of results returned. Limit is determined by the annual average number of vessels transiting through the port. If not provided, all ports are returned.

---
### Comando: `/economy/shipping/port_volume`

**Descripción:** Daily port calls and estimates of trading volumes for ports around the world.

- **Proveedores disponibles / soportados:** `econdb, imf`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `econdb`:*

  *Exclusivos del proveedor `imf`:*
  - `--port_code` (Opcional) `[str | None]`: Port code to filter results by a specific port. This parameter is ignored if `country` parameter is provided. To get a list of available ports, use `obb.economy.shipping.port_info()`.
  - `--country` (Opcional) `[Literal['ABW', 'AGO', 'AIA', 'ALB', 'ARE', 'ARG', 'ASM', 'ATG', 'AUS', 'AZE', 'BEL', 'BEN', 'BES', 'BGD', 'BGR', 'BHR', 'BHS', 'BLM', 'BLZ', 'BRA', 'BRB', 'BRN', 'CAN', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COK', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CUW', 'CYM', 'CYP', 'DEU', 'DJI', 'DMA', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESP', 'EST', 'FIN', 'FJI', 'FRA', 'FRO', 'FSM', 'GAB', 'GBR', 'GEO', 'GHA', 'GIB', 'GIN', 'GLP', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD', 'GTM', 'GUF', 'GUM', 'GUY', 'HKG', 'HND', 'HRV', 'HTI', 'IDN', 'IND', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LBN', 'LBR', 'LBY', 'LCA', 'LKA', 'LTU', 'LVA', 'MAC', 'MAF', 'MAR', 'MDA', 'MDG', 'MDV', 'MEX', 'MHL', 'MLT', 'MMR', 'MNE', 'MNP', 'MOZ', 'MRT', 'MSR', 'MTQ', 'MUS', 'MYS', 'MYT', 'NAM', 'NCL', 'NGA', 'NIC', 'NLD', 'NOR', 'NRU', 'NZL', 'OMN', 'PAK', 'PAN', 'PER', 'PHL', 'PLW', 'PNG', 'POL', 'PRI', 'PRT', 'PYF', 'QAT', 'REU', 'ROU', 'RUS', 'SAU', 'SDN', 'SEN', 'SGP', 'SLB', 'SLE', 'SLV', 'SOM', 'STP', 'SUR', 'SVN', 'SWE', 'SXM', 'SYC', 'SYR', 'TCA', 'TGO', 'THA', 'TKM', 'TLS', 'TON', 'TTO', 'TUN', 'TUR', 'TUV', 'TWN', 'TZA', 'UKR', 'URY', 'USA', 'VCT', 'VEN', 'VGB', 'VIR', 'VNM', 'VUT', 'WSM', 'YEM', 'ZAF'] | None]`: Country to focus on. Enter as a 3-letter ISO country code. This parameter is overridden by `port_code` if both are provided.

---
### Comando: `/economy/shipping/chokepoint_info`

**Descripción:** Get general metadata and statistics for all maritime chokepoint locations from a given provider.

- **Proveedores disponibles / soportados:** `imf`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `imf`:*
  - `--theme` (Opcional) `[Literal['dark', 'light'] | None]`: Theme for the map. Only valid if `openbb-charting` is installed and `chart` parameter is set to `true`. Default is the 'chart_style' setting in `user_settings.json`, if available, otherwise 'dark'.

---
### Comando: `/economy/shipping/chokepoint_volume`

**Descripción:** Daily transit calls and estimates of transit trade volumes for shipping lane chokepoints around the world.

- **Proveedores disponibles / soportados:** `imf`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `imf`:*
  - `--chokepoint` (Opcional) `[str | None]`: Name of the chokepoint. Use `None` for all chokepoints. Choices are:      - suez_canal     - panama_canal     - bosporus_strait     - bab_el_mandeb_strait     - malacca_strait     - strait_of_hormuz     - cape_of_good_hope     - gibraltar_strait     - dover_strait     - oresund_strait     - taiwan_strait     - korea_strait     - tsugaru_strait     - luzon_strait     - lombok_strait     - ombai_strait     - bohai_strait     - torres_strait     - sunda_strait     - makassar_strait     - magellan_strait     - yucatan_channel     - windward_passage     - mona_passage

---
### Comando: `/economy/survey/bls_series`

**Descripción:** Get time series data for one, or more, BLS series IDs.

- **Proveedores disponibles / soportados:** `bls`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): bls.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `bls`:*
  - `--calculations` (Opcional) `[bool | None]`: Include calculations in the response, if available. Default is True.
  - `--annual_average` (Opcional) `[bool | None]`: Include annual averages in the response, if available. Default is False.
  - `--aspects` (Opcional) `[bool | None]`: Include all aspects associated with a data point for a given BLS series ID, if available. Returned with the series metadata, under `extras` of the response object. Default is False.

---
### Comando: `/economy/survey/bls_search`

**Descripción:** Search BLS surveys by category and keyword or phrase to identify BLS series IDs.

- **Proveedores disponibles / soportados:** `bls`

**Flags / Parámetros (Standard & Providers):**
  - `--query` (Opcional) `[str | None]`: The search word(s). Use semi-colon to separate multiple queries as an & operator.

  *Exclusivos del proveedor `bls`:*
  - `--category` *(Requerido)* `[Literal['cpi', 'pce', 'ppi', 'ip', 'jolts', 'nfp', 'cps', 'lfs', 'wages', 'ec', 'sla', 'bed', 'tu']]`: The category of BLS survey to search within.         An empty search query will return all series within the category. Options are:              cpi - Consumer Price Index              pce - Personal Consumption Expenditure              ppi - Producer Price Index              ip - Industry Productivity              jolts - Job Openings and Labor Turnover Survey              nfp - Nonfarm Payrolls              cps - Current Population Survey              lfs - Labor Force Statistics              wages - Wages              ec - Employer Costs              sla - State and Local Area Employment              bed - Business Employment Dynamics              tu - Time Use
  - `--include_extras` (Opcional) `[bool | None]`: Include additional information in the search results. Extra fields returned are metadata and vary by survey. Fields are undefined strings that typically have names ending with '_code'.
  - `--include_code_map` (Opcional) `[bool | None]`: When True, includes the complete code map for eaçh survey in the category, returned separately as a nested JSON to the `extras['results_metadata']` property of the response. Example content is the NAICS industry map for PPI surveys. Each code is a value within the 'symbol' of the time series.

---
### Comando: `/economy/survey/sloos`

**Descripción:** Get Senior Loan Officers Opinion Survey.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--category` (Opcional) `[Literal['spreads', 'consumer', 'auto', 'credit_card', 'firms', 'mortgage', 'commercial_real_estate', 'standards', 'demand', 'foreign_banks'] | None]`: Category of survey response.
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log

---
### Comando: `/economy/survey/university_of_michigan`

**Descripción:** Get University of Michigan Consumer Sentiment and Inflation Expectations Surveys.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--frequency` (Opcional) `[Literal['quarter', 'annual'] | None]`: Frequency aggregation to convert monthly data to lower frequency. None is monthly.
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.              avg = Average              sum = Sum              eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type              None = No transformation              chg = Change              ch1 = Change from Year Ago              pch = Percent Change              pc1 = Percent Change from Year Ago              pca = Compounded Annual Rate of Change              cch = Continuously Compounded Rate of Change              cca = Continuously Compounded Annual Rate of Change              log = Natural Log

---
### Comando: `/economy/survey/economic_conditions_chicago`

**Descripción:** Get The Survey Of Economic Conditions For The Chicago Region.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--frequency` (Opcional) `[Literal['annual', 'quarter'] | None]`: Frequency aggregation to convert monthly data to lower frequency. None is monthly.
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.              avg = Average              sum = Sum              eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type              None = No transformation              chg = Change              ch1 = Change from Year Ago              pch = Percent Change              pc1 = Percent Change from Year Ago              pca = Compounded Annual Rate of Change              cch = Continuously Compounded Rate of Change              cca = Continuously Compounded Annual Rate of Change              log = Natural Log

---
### Comando: `/economy/survey/manufacturing_outlook_texas`

**Descripción:** Get The Manufacturing Outlook Survey For The Texas Region.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--topic` (Opcional) `[Literal['business_activity', 'business_outlook', 'capex', 'prices_paid', 'production', 'inventory', 'new_orders', 'new_orders_growth', 'unfilled_orders', 'shipments', 'delivery_time', 'employment', 'wages', 'hours_worked'] | None]`: The topic for the survey response.
  - `--frequency` (Opcional) `[Literal['annual', 'quarter'] | None]`: Frequency aggregation to convert monthly data to lower frequency. None is monthly.
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log

---
### Comando: `/economy/survey/manufacturing_outlook_ny`

**Descripción:** Get the Empire State Manufacturing Survey.

It is a monthly survey of manufacturers in New York State conducted by the Federal Reserve Bank of New York.

Participants from across the state in a variety of industries respond to a questionnaire
and report the change in a variety of indicators from the previous month.

Respondents also state the likely direction of these same indicators six months ahead.
April 2002 is the first report, although survey data date back to July 2001.

The survey is sent on the first day of each month to the same pool of about 200
manufacturing executives in New York State, typically the president or CEO.

About 100 responses are received. Most are completed by the tenth, although surveys are accepted until the fifteenth.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--topic` (Opcional) `[Literal['business_outlook', 'hours_worked', 'employment', 'inventories', 'prices_received', 'prices_paid', 'capex', 'unfilled_orders', 'new_orders', 'shipments', 'delivery_times'] | None]`: The topic for the survey response.
  - `--seasonally_adjusted` (Opcional) `[bool | None]`: Whether the data is seasonally adjusted, default is False
  - `--frequency` (Opcional) `[Literal['quarter', 'annual'] | None]`: Frequency aggregation to convert monthly data to lower frequency. None is monthly.
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.         avg = Average         sum = Sum         eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type         None = No transformation         chg = Change         ch1 = Change from Year Ago         pch = Percent Change         pc1 = Percent Change from Year Ago         pca = Compounded Annual Rate of Change         cch = Continuously Compounded Rate of Change         cca = Continuously Compounded Annual Rate of Change         log = Natural Log

---
### Comando: `/economy/survey/nonfarm_payrolls`

**Descripción:** Get Nonfarm Payrolls Survey.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--date` (Opcional) `[date | str | None | list[date | str | None]]`: A specific date to get data for. Default is the latest report. Multiple items allowed for provider(s): fred.

  *Exclusivos del proveedor `fred`:*
  - `--category` (Opcional) `[Literal['employees_nsa', 'employees_sa', 'employees_production_and_nonsupervisory', 'employees_women', 'employees_women_percent', 'avg_hours', 'avg_hours_production_and_nonsupervisory', 'avg_hours_overtime', 'avg_hours_overtime_production_and_nonsupervisory', 'avg_earnings_hourly', 'avg_earnings_hourly_production_and_nonsupervisory', 'avg_earnings_weekly', 'avg_earnings_weekly_production_and_nonsupervisory', 'index_weekly_hours', 'index_weekly_hours_production_and_nonsupervisory', 'index_weekly_payrolls', 'index_weekly_payrolls_production_and_nonsupervisory'] | None]`: The category to query.

---
### Comando: `/economy/calendar`

**Descripción:** Get the upcoming, or historical, economic calendar of global events.

- **Proveedores disponibles / soportados:** `fmp, nasdaq, tradingeconomics`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `nasdaq`:*
  - `--country` (Opcional) `[str | None]`: Country of the event

  *Exclusivos del proveedor `tradingeconomics`:*
  - `--country` (Opcional) `[str | None]`: Country of the event.
  - `--importance` (Opcional) `[Literal['low', 'medium', 'high'] | None]`: Importance of the event.
  - `--group` (Opcional) `[Literal['interest_rate', 'inflation', 'bonds', 'consumer', 'gdp', 'government', 'housing', 'labour', 'markets', 'money', 'prices', 'trade', 'business'] | None]`: Grouping of events.
  - `--calendar_id` (Opcional) `[None | int | str | None]`: Get events by TradingEconomics Calendar ID.

---
### Comando: `/economy/cpi`

**Descripción:** Get Consumer Price Index (CPI) data by country.

- **Proveedores disponibles / soportados:** `fred, imf, oecd`

**Flags / Parámetros (Standard & Providers):**
  - `--country` (Opcional) `[str | None | list[str | None]]`: The country to get data. Multiple items allowed for provider(s): fred, imf, oecd.
  - `--transform` (Opcional) `[str | None]`: Transformation of the CPI data.
  - `--frequency` (Opcional) `[Literal['annual', 'quarter', 'monthly'] | None]`: The frequency of the data.
  - `--harmonized` (Opcional) `[bool | None]`: If true, returns harmonized data.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*

  *Exclusivos del proveedor `imf`:*
  - `--expenditure` (Opcional) `[str | None]`: Expenditure component of CPI.
  - `--limit` (Opcional) `[int | None]`: Maximum number of records to retrieve per series and country. If None, retrieves all available records.

  *Exclusivos del proveedor `oecd`:*
  - `--expenditure` (Opcional) `[str | None]`: Expenditure component of CPI.

---
### Comando: `/economy/risk_premium`

**Descripción:** Get Market Risk Premium by country.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/economy/balance_of_payments`

**Descripción:** Balance of Payments Reports.

- **Proveedores disponibles / soportados:** `ecb, fred`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `ecb`:*
  - `--report_type` (Opcional) `[Literal['main', 'summary', 'services', 'investment_income', 'direct_investment', 'portfolio_investment', 'other_investment'] | None]`: The report type, the level of detail in the data.
  - `--frequency` (Opcional) `[Literal['monthly', 'quarterly'] | None]`: The frequency of the data.  Monthly is valid only for ['main', 'summary'].
  - `--country` (Opcional) `[Literal['brazil', 'canada', 'china', 'eu_ex_euro_area', 'eu_institutions', 'india', 'japan', 'russia', 'switzerland', 'united_kingdom', 'united_states', 'total'] | None]`: The country/region of the data.  This parameter will override the 'report_type' parameter.

  *Exclusivos del proveedor `fred`:*
  - `--country` (Opcional) `[Literal['argentina', 'australia', 'austria', 'belgium', 'brazil', 'canada', 'chile', 'china', 'colombia', 'costa_rica', 'czechia', 'denmark', 'estonia', 'finland', 'france', 'germany', 'greece', 'hungary', 'iceland', 'india', 'indonesia', 'ireland', 'israel', 'italy', 'japan', 'korea', 'latvia', 'lithuania', 'luxembourg', 'mexico', 'netherlands', 'new_zealand', 'norway', 'poland', 'portugal', 'russia', 'saudi_arabia', 'slovak_republic', 'slovenia', 'south_africa', 'spain', 'sweden', 'switzerland', 'turkey', 'united_kingdom', 'united_states', 'g7', 'g20'] | None]`: The country to get data. Enter as a 3-letter ISO country code, default is USA.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

---
### Comando: `/economy/fred_search`

**Descripción:** Search for FRED series or economic releases by ID or string.

This does not return the observation values, only the metadata.
Use this function to find series IDs for `fred_series()`.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--query` (Opcional) `[str | None]`: The search word(s).

  *Exclusivos del proveedor `fred`:*
  - `--search_type` (Opcional) `[Literal['full_text', 'series_id', 'release'] | None]`: The type of search to perform. Automatically set to 'release' when a 'release_id' is provided.
  - `--release_id` (Opcional) `[int | None]`: A specific release ID to target.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return. (1-1000)
  - `--offset` (Opcional) `[int | None]`: Offset the results in conjunction with limit. This parameter is ignored When search_type is 'release'.
  - `--order_by` (Opcional) `[Literal['search_rank', 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated', 'observation_start', 'observation_end', 'popularity', 'group_popularity'] | None]`: Order the results by a specific attribute. The default is 'observation_end'.
  - `--sort_order` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort the 'order_by' item in ascending or descending order. The default is 'desc'.
  - `--filter_variable` (Opcional) `[Literal['frequency', 'units', 'seasonal_adjustment'] | None]`: Filter by an attribute.
  - `--filter_value` (Opcional) `[str | None]`: String value to filter the variable by.  Used in conjunction with filter_variable. This parameter is ignored when search_type is 'release'.
  - `--tag_names` (Opcional) `[str | None]`: A semicolon delimited list of tag names that series match all of.  Example: 'japan;imports' This parameter is ignored when search_type is 'release'.
  - `--exclude_tag_names` (Opcional) `[str | None]`: A semicolon delimited list of tag names that series match none of.  Example: 'imports;services'. Requires that variable tag_names also be set to limit the number of matching series. This parameter is ignored when search_type is 'release'.
  - `--series_id` (Opcional) `[str | None]`: A FRED Series ID to return series group information for. This returns the required information to query for regional data. Not all series that are in FRED have geographical data. Entering a value for series_id will override all other parameters. Multiple series_ids can be separated by commas.

---
### Comando: `/economy/fred_series`

**Descripción:** Get data by series ID from FRED.

- **Proveedores disponibles / soportados:** `fred, intrinio`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): fred.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fred`:*
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.
  - `--frequency` (Opcional) `[Literal['a', 'q', 'm', 'w', 'd', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'] | None]`: Frequency aggregation to convert high frequency data to lower frequency.     None = No change     a = Annual     q = Quarterly     m = Monthly     w = Weekly     d = Daily     wef = Weekly, Ending Friday     weth = Weekly, Ending Thursday     wew = Weekly, Ending Wednesday     wetu = Weekly, Ending Tuesday     wem = Weekly, Ending Monday     wesu = Weekly, Ending Sunday     wesa = Weekly, Ending Saturday     bwew = Biweekly, Ending Wednesday     bwem = Biweekly, Ending Monday
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set.         avg = Average         sum = Sum         eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type     None = No transformation     chg = Change     ch1 = Change from Year Ago     pch = Percent Change     pc1 = Percent Change from Year Ago     pca = Compounded Annual Rate of Change     cch = Continuously Compounded Rate of Change     cca = Continuously Compounded Annual Rate of Change     log = Natural Log

  *Exclusivos del proveedor `intrinio`:*
  - `--all_pages` (Opcional) `[bool | None]`: Returns all pages of data from the API call at once.
  - `--sleep` (Opcional) `[float | None]`: Time to sleep between requests to avoid rate limiting.

---
### Comando: `/economy/fred_release_table`

**Descripción:** Get economic release data by ID and/or element from FRED.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--release_id` *(Requerido)* `[str]`: The ID of the release. Use `fred_search` to find releases.
  - `--element_id` (Opcional) `[str | None]`: The element ID of a specific table in the release.
  - `--date` (Opcional) `[None | date | str | None | list[None | date | str | None]]`: A specific date to get data for. Multiple items allowed for provider(s): fred.

  *Exclusivos del proveedor `fred`:*

---
### Comando: `/economy/money_measures`

**Descripción:** Get Money Measures (M1/M2 and components).

The Federal Reserve publishes as part of the H.6 Release.

- **Proveedores disponibles / soportados:** `federal_reserve`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--adjusted` (Opcional) `[bool | None]`: Whether to return seasonally adjusted data.

  *Exclusivos del proveedor `federal_reserve`:*

---
### Comando: `/economy/unemployment`

**Descripción:** Get global unemployment data.

- **Proveedores disponibles / soportados:** `oecd`

**Flags / Parámetros (Standard & Providers):**
  - `--country` (Opcional) `[str | None | list[str | None]]`: The country to get data. Multiple items allowed for provider(s): oecd.
  - `--frequency` (Opcional) `[Literal['monthly', 'quarter', 'annual'] | None]`: The frequency of the data.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `oecd`:*
  - `--country` (Opcional) `[str | None]`: The country to get data.
  - `--sex` (Opcional) `[Literal['total', 'male', 'female'] | None]`: Sex to get unemployment for.
  - `--age` (Opcional) `[Literal['total', '15-24', '25+'] | None]`: Age group to get unemployment for. Total indicates 15 years or over
  - `--seasonal_adjustment` (Opcional) `[bool | None]`: Whether to get seasonally adjusted unemployment. Defaults to False.

---
### Comando: `/economy/composite_leading_indicator`

**Descripción:** Get the composite leading indicator (CLI).

It is designed to provide early signals of turning points
in business cycles showing fluctuation of the economic activity around its long term potential level.

CLIs show short-term economic movements in qualitative rather than quantitative terms.

- **Proveedores disponibles / soportados:** `oecd`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `oecd`:*
  - `--country` (Opcional) `[Literal['g20', 'g7', 'asia5', 'north_america', 'europe4', 'australia', 'brazil', 'canada', 'china', 'france', 'germany', 'india', 'indonesia', 'italy', 'japan', 'mexico', 'south_africa', 'south_korea', 'spain', 'turkey', 'united_kingdom', 'united_states', 'all'] | None]`: Country to get the CLI for, default is G20.
  - `--adjustment` (Opcional) `[Literal['amplitude', 'normalized'] | None]`: Adjustment of the data, either 'amplitude' or 'normalized'. Default is amplitude.
  - `--growth_rate` (Opcional) `[bool | None]`: Return the 1-year growth rate (%) of the CLI, default is False.

---
### Comando: `/economy/fred_regional`

**Descripción:** Query the Geo Fred API for regional economic data by series group.

The series group ID is found by using `fred_search` and the `series_id` parameter.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fred`:*
  - `--symbol` *(Requerido)* `[str]`: For this function, it is the series_group ID or series ID. If the symbol provided is for a series_group, set the `is_series_group` parameter to True. Not all series that are in FRED have geographical data.
  - `--is_series_group` (Opcional) `[bool | None]`: When True, the symbol provided is for a series_group, else it is for a series ID.
  - `--region_type` (Opcional) `[Literal['bea', 'msa', 'frb', 'necta', 'state', 'country', 'county', 'censusregion'] | None]`: The type of regional data. Parameter is only valid when `is_series_group` is True.
  - `--season` (Opcional) `[Literal['sa', 'nsa', 'ssa'] | None]`: The seasonal adjustments to the data. Parameter is only valid when `is_series_group` is True.
  - `--units` (Opcional) `[str | None]`: The units of the data. This should match the units returned from searching by series ID. An incorrect field will not necessarily return an error. Parameter is only valid when `is_series_group` is True.
  - `--frequency` (Opcional) `[Literal['a', 'q', 'm', 'w', 'd', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'] | None]`: Frequency aggregation to convert high frequency data to lower frequency.              None = No change              a = Annual              q = Quarterly              m = Monthly              w = Weekly              d = Daily              wef = Weekly, Ending Friday              weth = Weekly, Ending Thursday              wew = Weekly, Ending Wednesday              wetu = Weekly, Ending Tuesday              wem = Weekly, Ending Monday              wesu = Weekly, Ending Sunday              wesa = Weekly, Ending Saturday              bwew = Biweekly, Ending Wednesday              bwem = Biweekly, Ending Monday
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set.              avg = Average              sum = Sum              eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type              None = No transformation              chg = Change              ch1 = Change from Year Ago              pch = Percent Change              pc1 = Percent Change from Year Ago              pca = Compounded Annual Rate of Change              cch = Continuously Compounded Rate of Change              cca = Continuously Compounded Annual Rate of Change              log = Natural Log

---
### Comando: `/economy/country_profile`

**Descripción:** Get a profile of country statistics and economic indicators.

- **Proveedores disponibles / soportados:** `econdb`

**Flags / Parámetros (Standard & Providers):**
  - `--country` *(Requerido)* `[str | list[str]]`: The country to get data. Multiple items allowed for provider(s): econdb.

  *Exclusivos del proveedor `econdb`:*
  - `--latest` (Opcional) `[bool | None]`: If True, return only the latest data. If False, return all available data for each indicator.
  - `--use_cache` (Opcional) `[bool | None]`: If True, the request will be cached for one day.Using cache is recommended to avoid needlessly requesting the same data.

---
### Comando: `/economy/available_indicators`

**Descripción:** Get the available economic indicators for a provider.

- **Proveedores disponibles / soportados:** `econdb, imf`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `econdb`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use cache or not, by default is True The cache of indicator symbols will persist for one week.

  *Exclusivos del proveedor `imf`:*
  - `--query` (Opcional) `[str | None]`: The search query string. Multiple search phrases can be separated by semicolons. Each phrase can use AND (+) and OR (|) operators, as well as quoted phrases. Semicolon separation allows commas to be used within search phrases.
  - `--dataflows` (Opcional) `[str | list[str] | None]`: list of IMF dataflow IDs to filter the indicators. Use semicolons to separate multiple dataflow IDs.
  - `--keywords` (Opcional) `[str | list[str] | None]`: list of keywords to filter results. Each keyword is a single word that must appear in the indicator's label or description. Keywords prefixed with 'not' will exclude indicators containing that word (e.g., 'not USD' excludes indicators with 'USD' in them).
  - `--symbol` (Opcional) `[str | None]`: Dummy field to allow grouping by symbol.

---
### Comando: `/economy/indicators`

**Descripción:** Get economic indicators by country and indicator.

- **Proveedores disponibles / soportados:** `econdb, imf`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): econdb, imf.
  - `--country` (Opcional) `[str | None | list[str | None]]`: The country to get data. Multiple items allowed for provider(s): econdb, imf.
  - `--frequency` (Opcional) `[str | None]`: The frequency of the data.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `econdb`:*
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for. The base symbol for the indicator (e.g. GDP, CPI, etc.). Use `available_indicators()` to get a list of available symbols.
  - `--country` (Opcional) `[str | None]`: The country to get data. ISO country codes or country names.
  - `--frequency` (Opcional) `[str | None]`: The frequency of the data, default is 'quarter'. Only valid when 'symbol' is 'main'.
  - `--transform` (Opcional) `[None | str | None]`: The transformation to apply to the data, default is None.      tpop: Change from previous period     toya: Change from one year ago     tusd: Values as US dollars     tpgp: Values as a percent of GDP      Only 'tpop' and 'toya' are applicable to all indicators. Applying transformations across multiple indicators/countries may produce unexpected results.     This is because not all indicators are compatible with all transformations, and the original units and scale differ between entities.     `tusd` should only be used where values are currencies.
  - `--use_cache` (Opcional) `[bool | None]`: If True, the request will be cached for one day. Using cache is recommended to avoid needlessly requesting the same data.

  *Exclusivos del proveedor `imf`:*
  - `--symbol` *(Requerido)* `[str | None]`: Symbol to get data for. Symbol format: 'dataflow::identifier' where identifier is either: - A table ID (starts with 'H_') for hierarchical table data - An indicator code for individual indicator data  Examples:     - 'BOP::H_BOP_BOP_AGG_STANDARD_PRESENTATION' - Balance of Payments table     - 'BOP_AGG::GS_CD,BOP_AGG::GS_DB' - Multiple BOP_AGG indicators (Goods & Services)     - 'IL::RGV_REVS' - Gold reserves in millions of fine troy ounces     - 'WEO::NGDP_RPCH' - Real GDP growth (annual only)     - 'WEO::POILBRE' - Brent crude oil price (use country='G001' for world)     - 'PCPS::PGOLD' - Gold price per troy ounce (monthly/quarterly available)  Use `obb.economy.available_indicators(provider='imf')` to discover symbols. Use `obb.economy.imf_utils.list_tables()` to see available tables.
  - `--country` (Opcional) `[str | None]`: ISO3 country code(s). Use comma-separated values for multiple countries. Validated against the dataflow's available countries via constraint API.
  - `--frequency` (Opcional) `[str | None]`: The frequency of the data. Choices vary by indicator and country. Common options: 'annual', 'quarter', 'month'. Use 'all' or '*' to return all available frequencies. Direct IMF codes (e.g., 'A', 'Q', 'M') are also accepted.
  - `--transform` (Opcional) `[str | None]`: Transformation to apply to the data. User-friendly options: 'index' (raw values), 'yoy' (year-over-year %), 'period' (period-over-period %). Use 'all' or '*' to return all available transformations. Direct IMF codes (e.g., 'USD', 'IX') are also accepted.
  - `--dimension_values` (Opcional) `[list[str] | None]`: list of additional dimension filters in 'DIM_ID:DIM_VALUE' format. Parameter can be entered multiple times.
  - `--limit` (Opcional) `[int | None]`: Maximum number of records to retrieve per series.
  - `--pivot` (Opcional) `[bool | None]`: If True, pivots the data to presentation view with 'indicator' and 'country' as the index, date as values.

---
### Comando: `/economy/central_bank_holdings`

**Descripción:** Get the balance sheet holdings of a central bank.

- **Proveedores disponibles / soportados:** `federal_reserve`

**Flags / Parámetros (Standard & Providers):**
  - `--date` (Opcional) `[date | None | str]`: A specific date to get data for.

  *Exclusivos del proveedor `federal_reserve`:*
  - `--holding_type` (Opcional) `[Literal['all_agency', 'agency_debts', 'mbs', 'cmbs', 'all_treasury', 'bills', 'notesbonds', 'frn', 'tips'] | None]`: Type of holdings to return.
  - `--summary` (Opcional) `[bool | None]`: If True, returns historical weekly summary by holding type. This parameter takes priority over other parameters.
  - `--cusip` (Opcional) `[str | None]`: 
  - `--wam` (Opcional) `[bool | None]`: If True, returns weighted average maturity aggregated by agency or treasury securities. This parameter takes priority over `holding_type`, `cusip`, and `monthly`.
  - `--monthly` (Opcional) `[bool | None]`: If True, returns historical data for all Treasury securities at a monthly interval. This parameter takes priority over other parameters, except `wam`. Only valid when `holding_type` is set to: 'all_treasury', 'bills', 'notesbonds', 'frn', 'tips'.

---
### Comando: `/economy/share_price_index`

**Descripción:** Get the Share Price Index by country from the OECD Short-Term Economics Statistics.

- **Proveedores disponibles / soportados:** `oecd`

**Flags / Parámetros (Standard & Providers):**
  - `--country` (Opcional) `[str | None | list[str | None]]`: The country to get data. Multiple items allowed for provider(s): oecd.
  - `--frequency` (Opcional) `[Literal['monthly', 'quarter', 'annual'] | None]`: The frequency of the data.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `oecd`:*
  - `--country` (Opcional) `[str | None]`: The country to get data.

---
### Comando: `/economy/house_price_index`

**Descripción:** Get the House Price Index by country from the OECD Short-Term Economics Statistics.

- **Proveedores disponibles / soportados:** `oecd`

**Flags / Parámetros (Standard & Providers):**
  - `--country` (Opcional) `[str | None | list[str | None]]`: The country to get data. Multiple items allowed for provider(s): oecd.
  - `--frequency` (Opcional) `[Literal['monthly', 'quarter', 'annual'] | None]`: The frequency of the data.
  - `--transform` (Opcional) `[Literal['index', 'yoy', 'period'] | None]`: Transformation of the CPI data. Period represents the change since previous. Defaults to change from one year ago (yoy).
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `oecd`:*
  - `--country` (Opcional) `[str | None]`: The country to get data.

---
### Comando: `/economy/interest_rates`

**Descripción:** Get interest rates by country(s) and duration.
Most OECD countries publish short-term, a long-term, and immediate rates monthly.

- **Proveedores disponibles / soportados:** `oecd`

**Flags / Parámetros (Standard & Providers):**
  - `--country` (Opcional) `[str | None | list[str | None]]`: The country to get data. Multiple items allowed for provider(s): oecd.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `oecd`:*
  - `--duration` (Opcional) `[Literal['immediate', 'short', 'long'] | None]`: Duration of the interest rate. 'immediate' is the overnight rate, 'short' is the 3-month rate, and 'long' is the 10-year rate.
  - `--frequency` (Opcional) `[Literal['monthly', 'quarter', 'annual'] | None]`: Frequency to get interest rate for for.

---
### Comando: `/economy/retail_prices`

**Descripción:** Get retail prices for common items.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--item` (Opcional) `[str | None]`: The item or basket of items to query.
  - `--country` (Opcional) `[str | None]`: The country to get data.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--item` (Opcional) `[Literal['beverages', 'cereals', 'dairy', 'fuel', 'produce', 'meats', 'bacon', 'bananas', 'beans', 'beef', 'beer', 'bread', 'butter', 'cheese', 'chicken', 'chops', 'coffee', 'cookies', 'corn', 'diesel', 'eggs', 'electricity', 'flour', 'gas', 'gasoline', 'grapefruit', 'ground_beef', 'ham', 'ice_cream', 'lemons', 'lettuce', 'malt_beverages', 'milk', 'oil', 'orange_juice', 'oranges', 'pork', 'potato_chips', 'potatoes', 'rice', 'soft_drinks', 'spaghetti', 'steak', 'strawberries', 'sugar', 'tomatoes', 'unleaded', 'usda', 'vodka', 'wine', 'yogurt'] | None]`: The item or basket of items to query.
  - `--country` (Opcional) `[Literal['united_states'] | None]`: The country to get data.
  - `--region` (Opcional) `[Literal['all_city', 'northeast', 'midwest', 'south', 'west'] | None]`: The region to get average price levels for.
  - `--frequency` (Opcional) `[Literal['annual', 'quarter', 'monthly'] | None]`: The frequency of the data.
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type     None = No transformation     chg = Change     ch1 = Change from Year Ago     pch = Percent Change     pc1 = Percent Change from Year Ago     pca = Compounded Annual Rate of Change     cch = Continuously Compounded Rate of Change     cca = Continuously Compounded Annual Rate of Change     log = Natural Log

---
### Comando: `/economy/primary_dealer_positioning`

**Descripción:** Get Primary dealer positioning statistics.

- **Proveedores disponibles / soportados:** `federal_reserve`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `federal_reserve`:*
  - `--category` (Opcional) `[Literal['treasuries', 'bills', 'coupons', 'notes', 'tips', 'mbs', 'cmbs', 'municipal', 'corporate', 'commercial_paper', 'corporate_ig', 'corporate_junk', 'abs'] | None]`: The category of asset to return, defaults to 'treasuries'.

---
### Comando: `/economy/pce`

**Descripción:** Get Personal Consumption Expenditures (PCE) reports.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--date` (Opcional) `[date | str | None | list[date | str | None]]`: A specific date to get data for. Default is the latest report. Multiple items allowed for provider(s): fred.

  *Exclusivos del proveedor `fred`:*
  - `--category` (Opcional) `[Literal['personal_income', 'wages_by_industry', 'real_pce_percent_change', 'real_pce_quantity_index', 'pce_price_index', 'pce_dollars', 'real_pce_chained_dollars', 'pce_price_percent_change'] | None]`: The category to query.

---
### Comando: `/economy/export_destinations`

**Descripción:** Get top export destinations by country from the UN Comtrade International Trade Statistics Database.

- **Proveedores disponibles / soportados:** `econdb`

**Flags / Parámetros (Standard & Providers):**
  - `--country` *(Requerido)* `[str | list[str]]`: The country to get data. Multiple items allowed for provider(s): econdb.

  *Exclusivos del proveedor `econdb`:*

---
### Comando: `/economy/primary_dealer_fails`

**Descripción:** Primary Dealer Statistics for Fails to Deliver and Fails to Receive.

Data from the NY Federal Reserve are updated on Thursdays at approximately
4:15 p.m. with the previous week's statistics.

For research on the topic, see:
https://www.federalreserve.gov/econres/notes/feds-notes/the-systemic-nature-of-settlement-fails-20170703.html

"Large and protracted settlement fails are believed to undermine the liquidity
and well-functioning of securities markets.

Near-100 percent pass-through of fails suggests a high degree of collateral
re-hypothecation together with the inability or unwillingness to borrow or buy the needed securities."

- **Proveedores disponibles / soportados:** `federal_reserve`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `federal_reserve`:*
  - `--asset_class` (Opcional) `[Literal['all', 'treasuries', 'tips', 'agency', 'mbs', 'corporate'] | None]`: Asset class to return, default is 'all'.
  - `--unit` (Opcional) `[Literal['value', 'percent'] | None]`: Unit of the data returned to the 'value' field. Default is 'value', which represents millions of USD. 'percent' returns data as the percentage of the total fails-to-receive and fails-to-deliver, by asset class.

---
### Comando: `/economy/direction_of_trade`

**Descripción:** Get Direction Of Trade Statistics from the IMF database.

The Direction of Trade Statistics (DOTS) presents the value of merchandise exports and
imports disaggregated according to a country's primary trading partners.
Area and world aggregates are included in the display of trade flows between major areas of the world.
Reported data is supplemented by estimates whenever such data is not available or current.
Imports are reported on a cost, insurance and freight (CIF) basis
and exports are reported on a free on board (FOB) basis.
Time series data includes estimates derived from reports of partner countries
for non-reporting and slow-reporting countries.

- **Proveedores disponibles / soportados:** `imf`

**Flags / Parámetros (Standard & Providers):**
  - `--country` (Opcional) `[str | None | list[str | None]]`: The country to get data. None is an equiavlent to 'all'. If 'all' is used, the counterpart field cannot be 'all'. Multiple items allowed for provider(s): imf.
  - `--counterpart` (Opcional) `[str | None | list[str | None]]`: Counterpart country to the trade. None is an equiavlent to 'all'. If 'all' is used, the country field cannot be 'all'. Multiple items allowed for provider(s): imf.
  - `--direction` (Opcional) `[Literal['exports', 'imports', 'balance', 'all'] | None]`: Trade direction. Use 'all' to get all data for this dimension.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--frequency` (Opcional) `[Literal['month', 'quarter', 'annual'] | None]`: The frequency of the data.

  *Exclusivos del proveedor `imf`:*
  - `--limit` (Opcional) `[int | None]`: Limit the number of results returned, the most recent data points first.

---
### Comando: `/economy/fomc_documents`

**Descripción:** Get lists of FOMC documents by year and document type.

Source: https://www.federalreserve.gov/monetarypolicy/fomc_historical.htm

Source: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm

- **Proveedores disponibles / soportados:** `federal_reserve`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `federal_reserve`:*
  - `--year` (Opcional) `[int | None]`: The year of FOMC documents to retrieve. If None, all years since 1959 are returned.
  - `--document_type` (Opcional) `[str | None]`: Filter by document type. Default is all. Choose from: all, monetary_policy, minutes, projections, materials, press_release, press_conference, agenda, transcript, speaker_key, beige_book, teal_book, green_book, blue_book, red_book
  - `--pdf_only` (Opcional) `[bool | None]`: Whether to return as a list with only the PDF documents. Default is False.
  - `--as_choices` (Opcional) `[bool | None]`: Whether to return cast as a list of valid Workspace parameter choices. Leave as False for typical use.

---
### Comando: `/equity/calendar/ipo`

**Descripción:** Get historical and upcoming initial public offerings (IPOs).

- **Proveedores disponibles / soportados:** `fmp, intrinio, nasdaq`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None]`: Symbol to get data for.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `intrinio`:*
  - `--status` (Opcional) `[Literal['upcoming', 'priced', 'withdrawn'] | None]`: Status of the IPO. [upcoming, priced, or withdrawn]
  - `--min_value` (Opcional) `[int | None]`: Return IPOs with an offer dollar amount greater than the given amount.
  - `--max_value` (Opcional) `[int | None]`: Return IPOs with an offer dollar amount less than the given amount.

  *Exclusivos del proveedor `nasdaq`:*
  - `--status` (Opcional) `[Literal['upcoming', 'priced', 'filed', 'withdrawn'] | None]`: The status of the IPO.
  - `--is_spo` (Opcional) `[bool | None]`: If True, returns data for secondary public offerings (SPOs).

---
### Comando: `/equity/calendar/dividend`

**Descripción:** Get historical and upcoming dividend payments. Includes dividend amount, ex-dividend and payment dates.

- **Proveedores disponibles / soportados:** `fmp, nasdaq`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `nasdaq`:*

---
### Comando: `/equity/calendar/splits`

**Descripción:** Get historical and upcoming stock split operations.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/equity/calendar/events`

**Descripción:** Get historical and upcoming company events, such as Investor Day, Conference Call, Earnings Release.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/equity/calendar/earnings`

**Descripción:** Get historical and upcoming company earnings releases. Includes earnings per share (EPS) and revenue data.

- **Proveedores disponibles / soportados:** `fmp, nasdaq, seeking_alpha, tmx`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `nasdaq`:*

  *Exclusivos del proveedor `seeking_alpha`:*
  - `--country` (Opcional) `[Literal['us', 'ca'] | None]`: The country to get calendar data for.

  *Exclusivos del proveedor `tmx`:*

---
### Comando: `/equity/compare/peers`

**Descripción:** Get the closest peers for a given company.

Peers consist of companies trading on the same exchange, operating within the same sector
and with comparable market capitalizations.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/equity/compare/groups`

**Descripción:** Get company data grouped by sector, industry or country and display either performance or valuation metrics.

Valuation metrics include price to earnings, price to book, price to sales ratios and price to cash flow.
Performance metrics include the stock price change for different time periods.

- **Proveedores disponibles / soportados:** `finviz`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `finviz`:*
  - `--group` (Opcional) `[Literal['sector', 'industry', 'country', 'capitalization', 'energy', 'materials', 'industrials', 'consumer_cyclical', 'consumer_defensive', 'healthcare', 'financial', 'technology', 'communication_services', 'utilities', 'real_estate'] | None]`: US-listed stocks only. When an individual sector is selected, it is broken down by industry. The default is 'sector'.
  - `--metric` (Opcional) `[Literal['performance', 'valuation', 'overview'] | None]`: Statistical metric to return. Select from: ['performance', 'valuation', 'overview'] The default is 'performance'.

---
### Comando: `/equity/compare/company_facts`

**Descripción:** Compare reported company facts and fundamental data points.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None | list[str | None]]`: Symbol to get data for. Multiple items allowed for provider(s): sec.
  - `--fact` (Opcional) `[str | None]`: The fact to lookup, typically a GAAP-reporting measure. Choices vary by provider.

  *Exclusivos del proveedor `sec`:*
  - `--fact` (Opcional) `[Literal['AccountsPayableCurrent', 'AccountsReceivableNet', 'AccountsReceivableNetCurrent', 'AccrualForTaxesOtherThanIncomeTaxesCurrent', 'AccrualForTaxesOtherThanIncomeTaxesCurrentAndNoncurrent', 'AccruedIncomeTaxesCurrent', 'AccruedIncomeTaxesNoncurrent', 'AccruedInsuranceCurrent', 'AccruedLiabilitiesCurrent', 'AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment', 'AccumulatedOtherComprehensiveIncomeLossNetOfTax', 'AcquisitionsNetOfCashAcquiredAndPurchasesOfIntangibleAndOtherAssets', 'AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue', 'AdvertisingExpense', 'AllocatedShareBasedCompensationExpense', 'AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount', 'Assets', 'AssetsCurrent', 'AssetsNoncurrent', 'NoncurrentAssets', 'AssetImpairmentCharges', 'BuildingsAndImprovementsGross', 'CapitalLeaseObligationsCurrent', 'CapitalLeaseObligationsNoncurrent', 'Cash', 'CashAndCashEquivalentsAtCarryingValue', 'CashCashEquivalentsAndShortTermInvestments', 'CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents', 'CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations', 'CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect', 'CommitmentsAndContingencies', 'CommercialPaper', 'CommonStockDividendsPerShareDeclared', 'CommonStockDividendsPerShareCashPaid', 'CommonStocksIncludingAdditionalPaidInCapital', 'ComprehensiveIncomeNetOfTax', 'ComprehensiveIncomeNetOfTaxAttributableToNoncontrollingInterest', 'ComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest', 'ConstructionInProgressGross', 'ContractWithCustomerAssetNet', 'ContractWithCustomerLiability', 'ContractWithCustomerLiabilityCurrent', 'ContractWithCustomerLiabilityNoncurrent', 'CostOfRevenue', 'CostOfGoodsAndServicesSold', 'CurrentFederalTaxExpenseBenefit', 'CurrentForeignTaxExpenseBenefit', 'CurrentIncomeTaxExpenseBenefit', 'CurrentStateAndLocalTaxExpenseBenefit', 'DebtInstrumentFaceAmount', 'DebtInstrumentFairValue', 'DebtLongtermAndShorttermCombinedAmount', 'DeferredFederalIncomeTaxExpenseBenefit', 'DeferredForeignIncomeTaxExpenseBenefit', 'DeferredIncomeTaxExpenseBenefit', 'DeferredIncomeTaxesAndTaxCredits', 'DeferredIncomeTaxLiabilities', 'DeferredIncomeTaxLiabilitiesNet', 'DeferredRevenue', 'DeferredTaxAssetsGross', 'DeferredTaxAssetsLiabilitiesNet', 'DeferredTaxAssetsNet', 'DeferredTaxLiabilities', 'DefinedContributionPlanCostRecognized', 'Depreciation', 'DepreciationAmortizationAndAccretionNet', 'DepreciationAmortizationAndOther', 'DepreciationAndAmortization', 'DepreciationDepletionAndAmortization', 'DerivativeCollateralObligationToReturnCash', 'DerivativeCollateralRightToReclaimCash', 'DerivativeFairValueOfDerivativeNet', 'DerivativeLiabilityCollateralRightToReclaimCashOffset', 'DerivativeNotionalAmount', 'Dividends', 'DividendsCash', 'DividendsPayableAmountPerShare', 'DividendsPayableCurrent', 'DistributedEarnings', 'EarningsPerShareBasic', 'EarningsPerShareDiluted', 'EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents', 'EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations', 'EmployeeRelatedLiabilitiesCurrent', 'EmployeeRelatedLiabilitiesCurrentAndNoncurrent', 'EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense', 'FinanceLeaseInterestExpense', 'FinanceLeaseInterestPaymentOnLiability', 'FinanceLeaseLiability', 'FinanceLeaseLiabilityCurrent', 'FinanceLeaseLiabilityNoncurrent', 'FinanceLeaseLiabilityPaymentsDue', 'FinanceLeaseLiabilityPaymentsDueAfterYearFive', 'FinanceLeaseLiabilityPaymentsDueNextTwelveMonths', 'FinanceLeaseLiabilityPaymentsDueYearFive', 'FinanceLeaseLiabilityPaymentsDueYearFour', 'FinanceLeaseLiabilityPaymentsDueYearThree', 'FinanceLeaseLiabilityPaymentsDueYearTwo', 'FinanceLeaseLiabilityPaymentsRemainderOfFiscalYear', 'FinanceLeaseLiabilityUndiscountedExcessAmount', 'FinanceLeasePrincipalPayments', 'FinanceLeaseRightOfUseAsset', 'FinancingReceivableAllowanceForCreditLosses', 'FiniteLivedIntangibleAssetsNet', 'FixturesAndEquipmentGross', 'GainLossOnInvestments', 'GainLossOnInvestmentsAndDerivativeInstruments', 'GainLossOnSaleOfBusiness', 'GainsLossesOnExtinguishmentOfDebt', 'GeneralAndAdministrativeExpense', 'Goodwill', 'GrossProfit', 'ImpairmentOfIntangibleAssetsExcludingGoodwill', 'ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill', 'IncomeLossFromContinuingOperations', 'IncomeLossFromContinuingOperationsAttributableToNoncontrollingEntity', 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest', 'IncomeLossFromContinuingOperationsPerBasicShare', 'IncomeLossFromContinuingOperationsPerDilutedShare', 'InterestAndDebtExpense', 'IncomeTaxExpenseBenefit', 'IncomeTaxesPaid', 'IncomeTaxesPaidNet', 'IncreaseDecreaseInAccountsAndOtherReceivables', 'IncreaseDecreaseInAccountsPayable', 'IncreaseDecreaseInAccountsReceivable', 'IncreaseDecreaseInAccruedLiabilities', 'IncreaseDecreaseInAccruedIncomeTaxesPayable', 'IncreaseDecreaseInAccruedTaxesPayable', 'IncreaseDecreaseInContractWithCustomerLiability', 'IncreaseDecreaseInDeferredIncomeTaxes', 'IncreaseDecreaseInInventories', 'IncreaseDecreaseInOtherCurrentAssets', 'IncreaseDecreaseInOtherCurrentLiabilities', 'IncreaseDecreaseInOtherNoncurrentAssets', 'IncreaseDecreaseInOtherNoncurrentLiabilities', 'IncreaseDecreaseInPensionPlanObligations', 'IncrementalCommonSharesAttributableToShareBasedPaymentArrangements', 'InterestExpenseDebt', 'InterestIncomeExpenseNet', 'InterestPaid', 'InterestPaidNet', 'InventoryNet', 'InvestmentIncomeInterest', 'Land', 'LeaseAndRentalExpense', 'LesseeOperatingLeaseLiabilityPaymentsDue', 'LesseeOperatingLeaseLiabilityPaymentsDueAfterYearFive', 'LesseeOperatingLeaseLiabilityPaymentsDueNextTwelveMonths', 'LesseeOperatingLeaseLiabilityPaymentsDueYearFive', 'LesseeOperatingLeaseLiabilityPaymentsDueYearFour', 'LesseeOperatingLeaseLiabilityPaymentsDueYearThree', 'LesseeOperatingLeaseLiabilityPaymentsDueYearTwo', 'LesseeOperatingLeaseLiabilityPaymentsRemainderOfFiscalYear', 'LettersOfCreditOutstandingAmount', 'Liabilities', 'LiabilitiesAndStockholdersEquity', 'LiabilitiesCurrent', 'LineOfCredit', 'LineOfCreditFacilityMaximumBorrowingCapacity', 'LongTermDebt', 'LongTermDebtCurrent', 'LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive', 'LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths', 'LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive', 'LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour', 'LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree', 'LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo', 'LongTermDebtMaturitiesRepaymentsOfPrincipalRemainderOfFiscalYear', 'LongTermDebtNoncurrent', 'LongTermInvestments', 'LossContingencyEstimateOfPossibleLoss', 'MachineryAndEquipmentGross', 'MarketableSecuritiesCurrent', 'MarketableSecuritiesNoncurrent', 'MinorityInterest', 'NetCashProvidedByUsedInFinancingActivities', 'NetCashProvidedByUsedInInvestingActivities', 'NetCashProvidedByUsedInOperatingActivities', 'NetIncomeLoss', 'NetIncomeLossAttributableToNoncontrollingInterest', 'NetIncomeLossAttributableToNonredeemableNoncontrollingInterest', 'NetIncomeLossAttributableToRedeemableNoncontrollingInterest', 'NonoperatingIncomeExpense', 'NoninterestIncome', 'NotesReceivableNet', 'OperatingExpenses', 'OperatingIncomeLoss', 'OperatingLeaseCost', 'OperatingLeaseLiability', 'OperatingLeaseLiabilityCurrent', 'OperatingLeaseLiabilityNoncurrent', 'OperatingLeaseRightOfUseAsset', 'OtherAccruedLiabilitiesCurrent', 'OtherAssetsCurrent', 'OtherAssetsNoncurrent', 'OtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentNetOfTax', 'OtherComprehensiveIncomeLossCashFlowHedgeGainLossAfterReclassificationAndTax', 'OtherComprehensiveIncomeLossDerivativeInstrumentGainLossafterReclassificationandTax', 'OtherComprehensiveIncomeLossDerivativeInstrumentGainLossbeforeReclassificationafterTax', 'OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax', 'OtherComprehensiveIncomeLossNetOfTax', 'OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent', 'OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodNetOfTax', 'OtherIncome', 'OtherLiabilitiesCurrent', 'OtherLiabilitiesNoncurrent', 'OtherLongTermDebt', 'OtherNoncashIncomeExpense', 'PaymentsForCapitalImprovements', 'PaymentsOfDividends', 'PaymentsOfDividendsMinorityInterest', 'PaymentsForProceedsFromBusinessesAndInterestInAffiliates', 'PaymentsForProceedsFromOtherInvestingActivities', 'PaymentsForRent', 'PaymentsForRepurchaseOfCommonStock', 'PaymentsOfDebtExtinguishmentCosts', 'PaymentsToAcquireInvestments', 'PaymentsToAcquirePropertyPlantAndEquipment', 'PreferredStockSharesOutstanding', 'PreferredStockValue', 'PrepaidExpenseAndOtherAssetsCurrent', 'PrepaidExpenseCurrent', 'ProceedsFromDebtMaturingInMoreThanThreeMonths', 'ProceedsFromDebtNetOfIssuanceCosts', 'ProceedsFromDivestitureOfBusinesses', 'ProceedsFromInvestments', 'ProceedsFromIssuanceOfCommonStock', 'ProceedsFromIssuanceOfDebt', 'ProceedsFromIssuanceOfLongTermDebt', 'ProceedsFromIssuanceOfUnsecuredDebt', 'ProceedsFromIssuanceOrSaleOfEquity', 'ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities', 'ProceedsFromPaymentsForOtherFinancingActivities', 'ProceedsFromPaymentsToMinorityShareholders', 'ProceedsFromRepaymentsOfShortTermDebt', 'ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLess', 'ProceedsFromSaleOfPropertyPlantAndEquipment', 'ProceedsFromStockOptionsExercised', 'ProfitLoss', 'PropertyPlantAndEquipmentGross', 'PropertyPlantAndEquipmentNet', 'ReceivablesNetCurrent', 'RedeemableNoncontrollingInterestEquityCarryingAmount', 'RepaymentsOfDebtMaturingInMoreThanThreeMonths', 'RepaymentsOfLongTermDebt', 'ResearchAndDevelopmentExpense', 'RestrictedCash', 'RestrictedCashAndCashEquivalents', 'RestrictedStockExpense', 'RestructuringCharges', 'RetainedEarningsAccumulatedDeficit', 'Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'SecuredLongTermDebt', 'SellingAndMarketingExpense', 'SellingGeneralAndAdministrativeExpense', 'ShareBasedCompensation', 'ShortTermBorrowings', 'ShortTermInvestments', 'StockholdersEquity', 'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest', 'StockholdersEquityOther', 'StockIssuedDuringPeriodValueNewIssues', 'StockOptionPlanExpense', 'StockRedeemedOrCalledDuringPeriodValue', 'StockRepurchasedDuringPeriodValue', 'StockRepurchasedAndRetiredDuringPeriodValue', 'TaxesPayableCurrent', 'TradingSecuritiesDebt', 'TreasuryStockAcquiredAverageCostPerShare', 'TreasuryStockSharesAcquired', 'UnrealizedGainLossOnInvestments', 'UnrecognizedTaxBenefits', 'UnsecuredDebt', 'VariableLeaseCost', 'WeightedAverageNumberOfDilutedSharesOutstanding', 'WeightedAverageNumberOfSharesOutstandingBasic', 'WeightedAverageNumberDilutedSharesOutstandingAdjustment'] | None]`: Fact or concept from the SEC taxonomy, in UpperCamelCase. Defaults to, 'Revenues'. AAPL, MSFT, GOOG, BRK-A currently report revenue as, 'RevenueFromContractWithCustomerExcludingAssessedTax'. In previous years, they have reported as 'Revenues'.
  - `--year` (Opcional) `[int | None]`: The year to retrieve the data for. If not provided, the current year is used. When symbol(s) are provided, excluding the year will return all reported values for the concept.
  - `--fiscal_period` (Opcional) `[Literal['fy', 'q1', 'q2', 'q3', 'q4'] | None]`: The fiscal period to retrieve the data for. If not provided, the most recent quarter is used. This parameter is ignored when a symbol is supplied.
  - `--instantaneous` (Opcional) `[bool | None]`: Whether to retrieve instantaneous data. See the notes above for more information. Defaults to False. Some facts are only available as instantaneous data. The function will automatically attempt the inverse of this parameter if the initial fiscal quarter request fails. This parameter is ignored when a symbol is supplied.
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use cache for the request. Defaults to True.

---
### Comando: `/equity/estimates/price_target`

**Descripción:** Get analyst price targets by company.

- **Proveedores disponibles / soportados:** `benzinga, finviz, fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None | list[str | None]]`: Symbol to get data for. Multiple items allowed for provider(s): benzinga, finviz, fmp.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `benzinga`:*
  - `--page` (Opcional) `[int | None]`: Page offset. For optimization, performance and technical reasons, page offsets are limited from 0 - 100000. Limit the query results by other parameters such as date. Used in conjunction with the limit and date parameters.
  - `--date` (Opcional) `[date | None | str]`: Date for calendar data, shorthand for date_from and date_to.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--updated` (Opcional) `[date | int | None]`: Records last Updated Unix timestamp (UTC). This will force the sort order to be Greater Than or Equal to the timestamp indicated. The date can be a date string or a Unix timestamp. The date string must be in the format of YYYY-MM-DD.
  - `--importance` (Opcional) `[int | None]`: Importance level to filter by. Uses Greater Than or Equal To the importance indicated
  - `--action` (Opcional) `[Literal['downgrades', 'maintains', 'reinstates', 'reiterates', 'upgrades', 'assumes', 'initiates', 'terminates', 'removes', 'suspends', 'firm_dissolved'] | None]`: Filter by a specific action_company.
  - `--analyst_ids` (Opcional) `[list[str] | str | None]`: Comma-separated list of analyst (person) IDs. Omitting will bring back all available analysts.
  - `--firm_ids` (Opcional) `[list[str] | str | None]`: Comma-separated list of firm IDs.
  - `--fields` (Opcional) `[list[str] | str | None]`: Comma-separated list of fields to include in the response. See https://docs.benzinga.io/benzinga-apis/calendar/get-ratings to learn about the available fields.

  *Exclusivos del proveedor `finviz`:*

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/equity/estimates/historical`

**Descripción:** Get historical analyst estimates for earnings and revenue.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp.

  *Exclusivos del proveedor `fmp`:*
  - `--period` (Opcional) `[Literal['quarter', 'annual'] | None]`: Time period of the data to return.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.
  - `--page` (Opcional) `[int | None]`: Page number for paginated results. Used with limit.

---
### Comando: `/equity/estimates/consensus`

**Descripción:** Get consensus price target and recommendation.

- **Proveedores disponibles / soportados:** `fmp, intrinio, tmx, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None | list[str | None]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp, intrinio, tmx, yfinance.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `intrinio`:*
  - `--industry_group_number` (Opcional) `[int | None]`: The Zacks industry group number.

  *Exclusivos del proveedor `tmx`:*

  *Exclusivos del proveedor `yfinance`:*

---
### Comando: `/equity/estimates/analyst_search`

**Descripción:** Search for specific analysts and get their forecast track record.

- **Proveedores disponibles / soportados:** `benzinga`

**Flags / Parámetros (Standard & Providers):**
  - `--analyst_name` (Opcional) `[str | None | list[str | None]]`: Analyst names to return. Omitting will return all available analysts. Multiple items allowed for provider(s): benzinga.
  - `--firm_name` (Opcional) `[str | None | list[str | None]]`: Firm names to return. Omitting will return all available firms. Multiple items allowed for provider(s): benzinga.

  *Exclusivos del proveedor `benzinga`:*
  - `--analyst_ids` (Opcional) `[str | None]`: list of analyst IDs to return.
  - `--firm_ids` (Opcional) `[str | None]`: Firm IDs to return.
  - `--limit` (Opcional) `[int | None]`: Number of results returned. Limit 1000.
  - `--page` (Opcional) `[int | None]`: Page offset. For optimization, performance and technical reasons, page offsets are limited from 0 - 100000. Limit the query results by other parameters such as date.
  - `--fields` (Opcional) `[str | None]`: Fields to include in the response. See https://docs.benzinga.io/benzinga-apis/calendar/get-ratings to learn about the available fields.

---
### Comando: `/equity/estimates/forward_sales`

**Descripción:** Get forward sales estimates.

- **Proveedores disponibles / soportados:** `intrinio, seeking_alpha`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None | list[str | None]]`: Symbol to get data for. Multiple items allowed for provider(s): intrinio, seeking_alpha.

  *Exclusivos del proveedor `intrinio`:*
  - `--fiscal_year` (Opcional) `[int | None]`: The future fiscal year to retrieve estimates for. When no symbol and year is supplied the current calendar year is used.
  - `--fiscal_period` (Opcional) `[Literal['fy', 'q1', 'q2', 'q3', 'q4'] | None]`: The future fiscal period to retrieve estimates for.
  - `--calendar_year` (Opcional) `[int | None]`: The future calendar year to retrieve estimates for. When no symbol and year is supplied the current calendar year is used.
  - `--calendar_period` (Opcional) `[Literal['q1', 'q2', 'q3', 'q4'] | None]`: The future calendar period to retrieve estimates for.

  *Exclusivos del proveedor `seeking_alpha`:*
  - `--period` (Opcional) `[Literal['annual', 'quarter'] | None]`: The reporting period.

---
### Comando: `/equity/estimates/forward_ebitda`

**Descripción:** Get forward EBITDA estimates.

- **Proveedores disponibles / soportados:** `fmp, intrinio`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None | list[str | None]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp, intrinio.

  *Exclusivos del proveedor `fmp`:*
  - `--fiscal_period` (Opcional) `[Literal['annual', 'quarter'] | None]`: The future fiscal period to retrieve estimates for.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return. Number of historical periods.
  - `--include_historical` (Opcional) `[bool | None]`: If True, the data will include all past data and the limit will be ignored.

  *Exclusivos del proveedor `intrinio`:*
  - `--fiscal_period` (Opcional) `[Literal['quarter', 'annual'] | None]`: Filter for only full-year or quarterly estimates.
  - `--estimate_type` (Opcional) `[Literal['ebitda', 'ebit', 'enterprise_value', 'cash_flow_per_share', 'pretax_income'] | None]`: Limit the EBITDA estimates to this type.

---
### Comando: `/equity/estimates/forward_eps`

**Descripción:** Get forward EPS estimates.

- **Proveedores disponibles / soportados:** `fmp, intrinio, seeking_alpha`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None | list[str | None]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp, intrinio, seeking_alpha.

  *Exclusivos del proveedor `fmp`:*
  - `--fiscal_period` (Opcional) `[Literal['annual', 'quarter'] | None]`: The future fiscal period to retrieve estimates for.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return. Number of historical periods.
  - `--include_historical` (Opcional) `[bool | None]`: If True, the data will include all past data and the limit will be ignored.

  *Exclusivos del proveedor `intrinio`:*
  - `--fiscal_year` (Opcional) `[int | None]`: The future fiscal year to retrieve estimates for. When no symbol and year is supplied the current calendar year is used.
  - `--fiscal_period` (Opcional) `[Literal['fy', 'q1', 'q2', 'q3', 'q4'] | None]`: The future fiscal period to retrieve estimates for.
  - `--calendar_year` (Opcional) `[int | None]`: The future calendar year to retrieve estimates for. When no symbol and year is supplied the current calendar year is used.
  - `--calendar_period` (Opcional) `[Literal['q1', 'q2', 'q3', 'q4'] | None]`: The future calendar period to retrieve estimates for.

  *Exclusivos del proveedor `seeking_alpha`:*
  - `--period` (Opcional) `[Literal['annual', 'quarter'] | None]`: The reporting period.

---
### Comando: `/equity/estimates/forward_pe`

**Descripción:** Get forward PE estimates.

- **Proveedores disponibles / soportados:** `intrinio`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None | list[str | None]]`: Symbol to get data for. Multiple items allowed for provider(s): intrinio.

  *Exclusivos del proveedor `intrinio`:*

---
### Comando: `/equity/darkpool/otc`

**Descripción:** Get the weekly aggregate trade data for Over The Counter deals.

ATS and non-ATS trading data for each ATS/firm
with trade reporting obligations under FINRA rules.

- **Proveedores disponibles / soportados:** `finra`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None]`: Symbol to get data for.

  *Exclusivos del proveedor `finra`:*
  - `--tier` (Opcional) `[Literal['T1', 'T2', 'OTCE'] | None]`: 'T1 - Securities included in the S&P 500, Russell 1000 and selected exchange-traded products;         T2 - All other NMS stocks; OTC - Over-the-Counter equity securities
  - `--is_ats` (Opcional) `[bool | None]`: ATS data if true, NON-ATS otherwise

---
### Comando: `/equity/discovery/gainers`

**Descripción:** Get the top price gainers in the stock market.

- **Proveedores disponibles / soportados:** `fmp, tmx, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `tmx`:*
  - `--category` (Opcional) `[Literal['dividend', 'energy', 'healthcare', 'industrials', 'price_performer', 'rising_stars', 'real_estate', 'tech', 'utilities', '52w_high', 'volume'] | None]`: The category of list to retrieve. Defaults to `price_performer`.

  *Exclusivos del proveedor `yfinance`:*
  - `--limit` (Opcional) `[int | None]`: Limit the number of results.

---
### Comando: `/equity/discovery/losers`

**Descripción:** Get the top price losers in the stock market.

- **Proveedores disponibles / soportados:** `fmp, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `yfinance`:*
  - `--limit` (Opcional) `[int | None]`: Limit the number of results.

---
### Comando: `/equity/discovery/active`

**Descripción:** Get the most actively traded stocks based on volume.

- **Proveedores disponibles / soportados:** `fmp, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `yfinance`:*
  - `--limit` (Opcional) `[int | None]`: Limit the number of results.

---
### Comando: `/equity/discovery/undervalued_large_caps`

**Descripción:** Get potentially undervalued large cap stocks.

- **Proveedores disponibles / soportados:** `yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.

  *Exclusivos del proveedor `yfinance`:*
  - `--limit` (Opcional) `[int | None]`: Limit the number of results.

---
### Comando: `/equity/discovery/undervalued_growth`

**Descripción:** Get potentially undervalued growth stocks.

- **Proveedores disponibles / soportados:** `yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.

  *Exclusivos del proveedor `yfinance`:*
  - `--limit` (Opcional) `[int | None]`: Limit the number of results.

---
### Comando: `/equity/discovery/aggressive_small_caps`

**Descripción:** Get top small cap stocks based on earnings growth.

- **Proveedores disponibles / soportados:** `yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.

  *Exclusivos del proveedor `yfinance`:*
  - `--limit` (Opcional) `[int | None]`: Limit the number of results. Default is all.

---
### Comando: `/equity/discovery/growth_tech`

**Descripción:** Get top tech stocks based on revenue and earnings growth.

- **Proveedores disponibles / soportados:** `yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.

  *Exclusivos del proveedor `yfinance`:*
  - `--limit` (Opcional) `[int | None]`: Limit the number of results.

---
### Comando: `/equity/discovery/top_retail`

**Descripción:** Track over $30B USD/day of individual investors trades.

It gives a daily view into retail activity and sentiment for over 9,500 US traded stocks,
ADRs, and ETPs.

- **Proveedores disponibles / soportados:** `nasdaq`

**Flags / Parámetros (Standard & Providers):**
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `nasdaq`:*

---
### Comando: `/equity/discovery/filings`

**Descripción:** Get the URLs to SEC filings reported to EDGAR database, such as 10-K, 10-Q, 8-K, and more.

SEC filings include Form 10-K, Form 10-Q, Form 8-K, the proxy statement, Forms 3, 4, and 5, Schedule 13, Form 114,
Foreign Investment Disclosures and others. The annual 10-K report is required to be
filed annually and includes the company's financial statements, management discussion and analysis,
and audited financial statements.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--form_type` (Opcional) `[str | None]`: Filter by form type. Visit https://www.sec.gov/forms for a list of supported form types.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*
  - `--limit` (Opcional) `[int | None]`: The maximum number of results to return. Default is 10000.

---
### Comando: `/equity/discovery/latest_financial_reports`

**Descripción:** Get the newest quarterly, annual, and current reports for all companies.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `sec`:*
  - `--date` (Opcional) `[date | None | str]`: A specific date to get data for. Defaults to today.
  - `--report_type` (Opcional) `[str | None]`: Return only a specific form type. Default is all quarterly, annual, and current reports. Choices: 1-K, 1-SA, 1-U, 10-D, 10-K, 10-KT, 10-Q, 10-QT, 20-F, 40-F, 6-K, 8-K.

---
### Comando: `/equity/fundamental/balance`

**Descripción:** Get the balance sheet for a given company.

- **Proveedores disponibles / soportados:** `fmp, intrinio, polygon, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*
  - `--period` (Opcional) `[Literal['q1', 'q2', 'q3', 'q4', 'fy', 'ttm', 'annual', 'quarter'] | None]`: Time period of the data to return.

  *Exclusivos del proveedor `intrinio`:*
  - `--period` (Opcional) `[Literal['annual', 'quarter'] | None]`: Time period of the data to return.
  - `--fiscal_year` (Opcional) `[int | None]`: The specific fiscal year.  Reports do not go beyond 2008.

  *Exclusivos del proveedor `polygon`:*
  - `--period` (Opcional) `[Literal['annual', 'quarter'] | None]`: Time period of the data to return.
  - `--filing_date` (Opcional) `[date | None]`: Filing date of the financial statement.
  - `--filing_date_lt` (Opcional) `[date | None]`: Filing date less than the given date.
  - `--filing_date_lte` (Opcional) `[date | None]`: Filing date less than or equal to the given date.
  - `--filing_date_gt` (Opcional) `[date | None]`: Filing date greater than the given date.
  - `--filing_date_gte` (Opcional) `[date | None]`: Filing date greater than or equal to the given date.
  - `--period_of_report_date` (Opcional) `[date | None]`: Period of report date of the financial statement.
  - `--period_of_report_date_lt` (Opcional) `[date | None]`: Period of report date less than the given date.
  - `--period_of_report_date_lte` (Opcional) `[date | None]`: Period of report date less than or equal to the given date.
  - `--period_of_report_date_gt` (Opcional) `[date | None]`: Period of report date greater than the given date.
  - `--period_of_report_date_gte` (Opcional) `[date | None]`: Period of report date greater than or equal to the given date.
  - `--include_sources` (Opcional) `[bool | None]`: Whether to include the sources of the financial statement.
  - `--order` (Opcional) `[Literal['asc', 'desc'] | None]`: Order of the financial statement.
  - `--sort` (Opcional) `[Literal['filing_date', 'period_of_report_date'] | None]`: Sort of the financial statement.

  *Exclusivos del proveedor `yfinance`:*
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.
  - `--period` (Opcional) `[Literal['annual', 'quarter'] | None]`: Time period of the data to return.

---
### Comando: `/equity/fundamental/balance_growth`

**Descripción:** Get the growth of a company's balance sheet items over time.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return. (default 5)
  - `--period` (Opcional) `[Literal['q1', 'q2', 'q3', 'q4', 'fy', 'annual', 'quarter'] | None]`: Time period of the data to return.

---
### Comando: `/equity/fundamental/cash`

**Descripción:** Get the cash flow statement for a given company.

- **Proveedores disponibles / soportados:** `fmp, intrinio, polygon, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*
  - `--period` (Opcional) `[Literal['q1', 'q2', 'q3', 'q4', 'fy', 'ttm', 'annual', 'quarter'] | None]`: Time period of the data to return.

  *Exclusivos del proveedor `intrinio`:*
  - `--period` (Opcional) `[Literal['annual', 'quarter', 'ttm', 'ytd'] | None]`: Time period of the data to return.
  - `--fiscal_year` (Opcional) `[int | None]`: The specific fiscal year.  Reports do not go beyond 2008.

  *Exclusivos del proveedor `polygon`:*
  - `--period` (Opcional) `[Literal['annual', 'quarter', 'ttm'] | None]`: Time period of the data to return.
  - `--filing_date` (Opcional) `[date | None]`: Filing date of the financial statement.
  - `--filing_date_lt` (Opcional) `[date | None]`: Filing date less than the given date.
  - `--filing_date_lte` (Opcional) `[date | None]`: Filing date less than or equal to the given date.
  - `--filing_date_gt` (Opcional) `[date | None]`: Filing date greater than the given date.
  - `--filing_date_gte` (Opcional) `[date | None]`: Filing date greater than or equal to the given date.
  - `--period_of_report_date` (Opcional) `[date | None]`: Period of report date of the financial statement.
  - `--period_of_report_date_lt` (Opcional) `[date | None]`: Period of report date less than the given date.
  - `--period_of_report_date_lte` (Opcional) `[date | None]`: Period of report date less than or equal to the given date.
  - `--period_of_report_date_gt` (Opcional) `[date | None]`: Period of report date greater than the given date.
  - `--period_of_report_date_gte` (Opcional) `[date | None]`: Period of report date greater than or equal to the given date.
  - `--include_sources` (Opcional) `[bool | None]`: Whether to include the sources of the financial statement.
  - `--order` (Opcional) `[Literal['asc', 'desc'] | None]`: Order of the financial statement.
  - `--sort` (Opcional) `[Literal['filing_date', 'period_of_report_date'] | None]`: Sort of the financial statement.

  *Exclusivos del proveedor `yfinance`:*
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.
  - `--period` (Opcional) `[Literal['annual', 'quarter'] | None]`: Time period of the data to return.

---
### Comando: `/equity/fundamental/reported_financials`

**Descripción:** Get financial statements as reported by the company.

- **Proveedores disponibles / soportados:** `intrinio`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--period` (Opcional) `[str | None]`: Time period of the data to return.
  - `--statement_type` (Opcional) `[str | None]`: The type of financial statement - i.e, balance, income, cash.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return. Although the response object contains multiple results, because of the variance in the fields, year-to-year and quarter-to-quarter, it is recommended to view results in small chunks.

  *Exclusivos del proveedor `intrinio`:*
  - `--period` (Opcional) `[Literal['annual', 'quarter'] | None]`: None
  - `--statement_type` (Opcional) `[Literal['balance', 'income', 'cash'] | None]`: Cash flow statements are reported as YTD, Q4 is the same as FY.
  - `--fiscal_year` (Opcional) `[int | None]`: The specific fiscal year.  Reports do not go beyond 2008.

---
### Comando: `/equity/fundamental/cash_growth`

**Descripción:** Get the growth of a company's cash flow statement items over time.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*
  - `--period` (Opcional) `[Literal['q1', 'q2', 'q3', 'q4', 'fy', 'annual', 'quarter'] | None]`: Time period of the data to return.

---
### Comando: `/equity/fundamental/dividends`

**Descripción:** Get historical dividend data for a given company.

- **Proveedores disponibles / soportados:** `fmp, intrinio, nasdaq, tmx, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp, nasdaq.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fmp`:*
  - `--limit` (Opcional) `[int | None]`: Return N most recent payments.

  *Exclusivos del proveedor `intrinio`:*
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `nasdaq`:*

  *Exclusivos del proveedor `tmx`:*

  *Exclusivos del proveedor `yfinance`:*

---
### Comando: `/equity/fundamental/historical_eps`

**Descripción:** Get historical earnings per share data for a given company.

- **Proveedores disponibles / soportados:** `alpha_vantage, fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): alpha_vantage, fmp.

  *Exclusivos del proveedor `alpha_vantage`:*
  - `--period` (Opcional) `[Literal['annual', 'quarter'] | None]`: Time period of the data to return.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return. Default is all.

---
### Comando: `/equity/fundamental/employee_count`

**Descripción:** Get historical employee count data for a given company.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fmp`:*
  - `--limit` (Opcional) `[int | None]`: Number of records to return. Default is all.

---
### Comando: `/equity/fundamental/search_attributes`

**Descripción:** Search Intrinio data tags to search in latest or historical attributes.

- **Proveedores disponibles / soportados:** `intrinio`

**Flags / Parámetros (Standard & Providers):**
  - `--query` *(Requerido)* `[str]`: Query to search for.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `intrinio`:*

---
### Comando: `/equity/fundamental/latest_attributes`

**Descripción:** Get the latest value of a data tag from Intrinio.

- **Proveedores disponibles / soportados:** `intrinio`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): intrinio.
  - `--tag` *(Requerido)* `[str | list[str]]`: Intrinio data tag ID or code. Multiple items allowed for provider(s): intrinio.

  *Exclusivos del proveedor `intrinio`:*

---
### Comando: `/equity/fundamental/historical_attributes`

**Descripción:** Get the historical values of a data tag from Intrinio.

- **Proveedores disponibles / soportados:** `intrinio`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): intrinio.
  - `--tag` *(Requerido)* `[str | list[str]]`: Intrinio data tag ID or code. Multiple items allowed for provider(s): intrinio.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--frequency` (Opcional) `[Literal['daily', 'weekly', 'monthly', 'quarterly', 'yearly'] | None]`: The frequency of the data.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.
  - `--tag_type` (Opcional) `[str | None]`: Filter by type, when applicable.
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order.

  *Exclusivos del proveedor `intrinio`:*

---
### Comando: `/equity/fundamental/income`

**Descripción:** Get the income statement for a given company.

- **Proveedores disponibles / soportados:** `fmp, intrinio, polygon, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*
  - `--period` (Opcional) `[Literal['q1', 'q2', 'q3', 'q4', 'fy', 'ttm', 'annual', 'quarter'] | None]`: Time period of the data to return.

  *Exclusivos del proveedor `intrinio`:*
  - `--period` (Opcional) `[Literal['annual', 'quarter', 'ttm', 'ytd'] | None]`: Time period of the data to return.
  - `--fiscal_year` (Opcional) `[int | None]`: The specific fiscal year.  Reports do not go beyond 2008.

  *Exclusivos del proveedor `polygon`:*
  - `--period` (Opcional) `[Literal['annual', 'quarter', 'ttm'] | None]`: Time period of the data to return.
  - `--filing_date` (Opcional) `[date | None]`: Filing date of the financial statement.
  - `--filing_date_lt` (Opcional) `[date | None]`: Filing date less than the given date.
  - `--filing_date_lte` (Opcional) `[date | None]`: Filing date less than or equal to the given date.
  - `--filing_date_gt` (Opcional) `[date | None]`: Filing date greater than the given date.
  - `--filing_date_gte` (Opcional) `[date | None]`: Filing date greater than or equal to the given date.
  - `--period_of_report_date` (Opcional) `[date | None]`: Period of report date of the financial statement.
  - `--period_of_report_date_lt` (Opcional) `[date | None]`: Period of report date less than the given date.
  - `--period_of_report_date_lte` (Opcional) `[date | None]`: Period of report date less than or equal to the given date.
  - `--period_of_report_date_gt` (Opcional) `[date | None]`: Period of report date greater than the given date.
  - `--period_of_report_date_gte` (Opcional) `[date | None]`: Period of report date greater than or equal to the given date.
  - `--include_sources` (Opcional) `[bool | None]`: Whether to include the sources of the financial statement.
  - `--order` (Opcional) `[Literal['asc', 'desc'] | None]`: Order of the financial statement.
  - `--sort` (Opcional) `[Literal['filing_date', 'period_of_report_date'] | None]`: Sort of the financial statement.

  *Exclusivos del proveedor `yfinance`:*
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.
  - `--period` (Opcional) `[Literal['annual', 'quarter'] | None]`: Time period of the data to return.

---
### Comando: `/equity/fundamental/income_growth`

**Descripción:** Get the growth of a company's income statement items over time.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*
  - `--period` (Opcional) `[Literal['q1', 'q2', 'q3', 'q4', 'fy', 'annual', 'quarter'] | None]`: Time period of the data to return.

---
### Comando: `/equity/fundamental/metrics`

**Descripción:** Get fundamental metrics for a given company.

- **Proveedores disponibles / soportados:** `finviz, fmp, intrinio, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): finviz, fmp, intrinio, yfinance.

  *Exclusivos del proveedor `finviz`:*

  *Exclusivos del proveedor `fmp`:*
  - `--ttm` (Opcional) `[Literal['include', 'exclude', 'only'] | None]`: Specify whether to include, exclude, or only show TTM (Trailing Twelve Months) data. The default is 'only'.
  - `--period` (Opcional) `[Literal['q1', 'q2', 'q3', 'q4', 'fy', 'annual', 'quarter'] | None]`: Specify the fiscal period for the data. Ignored when TTM is set to 'only'.
  - `--limit` (Opcional) `[int | None]`: Only applicable when TTM is not set to 'only'. Defines the number of most recent reporting periods to return. The default is 5.

  *Exclusivos del proveedor `intrinio`:*

  *Exclusivos del proveedor `yfinance`:*

---
### Comando: `/equity/fundamental/management`

**Descripción:** Get executive management team data for a given company.

- **Proveedores disponibles / soportados:** `fmp, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `yfinance`:*

---
### Comando: `/equity/fundamental/management_compensation`

**Descripción:** Get executive management team compensation for a given company over time.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp.

  *Exclusivos del proveedor `fmp`:*
  - `--year` (Opcional) `[int | None]`: Filters results by year, enter 0 for all data available. Default is the most recent year in the dataset, -1.

---
### Comando: `/equity/fundamental/ratios`

**Descripción:** Get an extensive set of financial and accounting ratios for a given company over time.

- **Proveedores disponibles / soportados:** `fmp, intrinio`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*
  - `--limit` (Opcional) `[int | None]`: Only applicable when TTM is not set to 'only'. Defines the number of most recent reporting periods to return. The default is 5.
  - `--ttm` (Opcional) `[Literal['include', 'exclude', 'only'] | None]`: Specify whether to include, exclude, or only show TTM (Trailing Twelve Months) data. The default is 'only'.
  - `--period` (Opcional) `[Literal['q1', 'q2', 'q3', 'q4', 'fy', 'annual', 'quarter'] | None]`: Specify the fiscal period for the data.

  *Exclusivos del proveedor `intrinio`:*
  - `--period` (Opcional) `[Literal['annual', 'quarter', 'ttm', 'ytd'] | None]`: Time period of the data to return.
  - `--fiscal_year` (Opcional) `[int | None]`: The specific fiscal year.  Reports do not go beyond 2008.

---
### Comando: `/equity/fundamental/revenue_per_geography`

**Descripción:** Get the geographic breakdown of revenue for a given company over time.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `fmp`:*
  - `--period` (Opcional) `[Literal['quarter', 'annual'] | None]`: Time period of the data to return.

---
### Comando: `/equity/fundamental/revenue_per_segment`

**Descripción:** Get the revenue breakdown by business segment for a given company over time.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `fmp`:*
  - `--period` (Opcional) `[Literal['quarter', 'annual'] | None]`: Time period of the data to return.

---
### Comando: `/equity/fundamental/filings`

**Descripción:** Get public company filings.

- **Proveedores disponibles / soportados:** `fmp, intrinio, nasdaq, sec, tmx`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None]`: Symbol to get data for.

  *Exclusivos del proveedor `fmp`:*
  - `--cik` (Opcional) `[str | None]`: CIK number to look up. Overrides symbol.
  - `--start_date` (Opcional) `[date | None | str]`: Start date for filtering filings. Default is one year ago.
  - `--end_date` (Opcional) `[date | None | str]`: End date for filtering filings.
  - `--limit` (Opcional) `[int | None]`: Number of results to return. Max results is 1000.
  - `--page` (Opcional) `[int | None]`: Page number for paginated results. Max page is 100.

  *Exclusivos del proveedor `intrinio`:*
  - `--form_type` (Opcional) `[str | None]`: SEC form type to filter by.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.
  - `--thea_enabled` (Opcional) `[bool | None]`: Return filings that have been read by Intrinio's Thea NLP.

  *Exclusivos del proveedor `nasdaq`:*
  - `--year` (Opcional) `[int | None]`: Calendar year of the data, default is current year. The earliest year available is 1994, for all companies and form types.
  - `--form_group` (Opcional) `[Literal['annual', 'quarterly', 'proxy', 'insider', '8k', 'registration', 'comment'] | None]`: The form group to fetch, default is 8k.

  *Exclusivos del proveedor `sec`:*
  - `--cik` (Opcional) `[str | int | None]`: Lookup filings by Central Index Key (CIK) instead of by symbol.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--form_type` (Opcional) `[str | None]`: SEC form type to filter by.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.
  - `--use_cache` (Opcional) `[bool | None]`: Whether or not to use cache.  If True, cache will store for one day.

  *Exclusivos del proveedor `tmx`:*
  - `--start_date` (Opcional) `[date | None | str]`: The start date to fetch.
  - `--end_date` (Opcional) `[date | None | str]`: The end date to fetch.

---
### Comando: `/equity/fundamental/historical_splits`

**Descripción:** Get historical stock splits for a given company.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/equity/fundamental/transcript`

**Descripción:** Get earnings call transcripts for a given company.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--year` (Opcional) `[int | None]`: Year of the earnings call transcript.
  - `--quarter` (Opcional) `[Literal[1, 2, 3, 4] | None]`: Quarterly period of the earnings call transcript.

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/equity/fundamental/trailing_dividend_yield`

**Descripción:** Get the 1 year trailing dividend yield for a given company over time.

- **Proveedores disponibles / soportados:** `tiingo`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return. Default is 252, the number of trading days in a year.

  *Exclusivos del proveedor `tiingo`:*

---
### Comando: `/equity/fundamental/management_discussion_analysis`

**Descripción:** Get the Management Discussion & Analysis section from the financial statements for a given company.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--calendar_year` (Opcional) `[int | None]`: Calendar year of the report. By default, is the current year. If the calendar period is not provided, but the calendar year is, it will return the annual report.
  - `--calendar_period` (Opcional) `[Literal['Q1', 'Q2', 'Q3', 'Q4'] | None]`: Calendar period of the report. By default, is the most recent report available for the symbol. If no calendar year and no calendar period are provided, it will return the most recent report.

  *Exclusivos del proveedor `sec`:*
  - `--strategy` (Opcional) `[Literal['inscriptis', 'trafilatura'] | None]`: The strategy to use for extracting the text. Default is 'trafilatura'.
  - `--wrap_length` (Opcional) `[int | None]`: The length to wrap the extracted text, excluding tables. Default is 120.
  - `--include_tables` (Opcional) `[bool | None]`: Return tables formatted as markdown in the text. Default is False. Tables may reveal 'missing' content, but will likely need some level of manual cleaning, post-request, to display properly. In some cases, tables may not be recoverable due to the nature of the document.
  - `--use_cache` (Opcional) `[bool | None]`: When True, the file will be cached for use later. Default is True.
  - `--raw_html` (Opcional) `[bool | None]`: When True, the raw HTML content of the entire filing will be returned. Default is False. Use this option to parse the document manually.

---
### Comando: `/equity/fundamental/esg_score`

**Descripción:** Get ESG (Environmental, Social, and Governance) scores from company disclosures.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp.

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/equity/ownership/major_holders`

**Descripción:** Get data about major holders for a given company over time.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `fmp`:*
  - `--year` (Opcional) `[int | None]`: Calendar year for the data. If not provided, the latest year is used.
  - `--quarter` (Opcional) `[int | None]`: Calendar quarter for the data. Valid values are 1, 2, 3, or 4. If not provided, the quarter previous to the current quarter is used.
  - `--page` (Opcional) `[int | None]`: Page number, used in conjunction with the limit. The default is 0.
  - `--limit` (Opcional) `[int | None]`: Number of items to return per page. The default is 100, which is the maximum.

---
### Comando: `/equity/ownership/institutional`

**Descripción:** Net statistics on institutional ownership for a given company, reported on 13-F filings.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp.

  *Exclusivos del proveedor `fmp`:*
  - `--year` (Opcional) `[int | None]`: Calendar year for the data. If not provided, the latest year is used.
  - `--quarter` (Opcional) `[int | None]`: Calendar quarter for the data. Valid values are 1, 2, 3, or 4. If not provided, the quarter previous to the current quarter is used.

---
### Comando: `/equity/ownership/insider_trading`

**Descripción:** Get data about trading by a company's management team and board of directors.

- **Proveedores disponibles / soportados:** `fmp, intrinio, sec, tmx`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*
  - `--transaction_type` (Opcional) `[Literal['award', 'conversion', 'return', 'expire_short', 'in_kind', 'gift', 'expire_long', 'discretionary', 'other', 'small', 'exempt', 'otm', 'purchase', 'sale', 'tender', 'will', 'itm', 'trust'] | None]`: Type of the transaction.
  - `--statistics` (Opcional) `[bool | None]`: Flag to return summary statistics for the given symbol. Setting as True will ignore other parameters except symbol.

  *Exclusivos del proveedor `intrinio`:*
  - `--start_date` *(Requerido)* `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` *(Requerido)* `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--ownership_type` (Opcional) `[Literal['D', 'I'] | None]`: Type of ownership.
  - `--sort_by` (Opcional) `[Literal['filing_date', 'updated_on'] | None]`: Field to sort by.

  *Exclusivos del proveedor `sec`:*
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format. Wide date ranges can result in long download times. Recommended to use a smaller date range, default is 120 days ago.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format. Default is today.
  - `--use_cache` (Opcional) `[bool | None]`: Persist the data locally for future use. Default is True. Each form submission is an individual download and the SEC limits the number of concurrent downloads. This prevents the same file from being downloaded multiple times.

  *Exclusivos del proveedor `tmx`:*
  - `--summary` (Opcional) `[bool | None]`: Return a summary of the insider activity instead of the individuals.

---
### Comando: `/equity/ownership/share_statistics`

**Descripción:** Get data about share float for a given company.

- **Proveedores disponibles / soportados:** `fmp, intrinio, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp, yfinance.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `intrinio`:*

  *Exclusivos del proveedor `yfinance`:*

---
### Comando: `/equity/ownership/form_13f`

**Descripción:** Get the form 13F.

The Securities and Exchange Commission's (SEC) Form 13F is a quarterly report
that is required to be filed by all institutional investment managers with at least
$100 million in assets under management.
Managers are required to file Form 13F within 45 days after the last day of the calendar quarter.
Most funds wait until the end of this period in order to conceal
their investment strategy from competitors and the public.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for. A CIK or Symbol can be used.
  - `--date` (Opcional) `[date | None | str]`: A specific date to get data for. The date represents the end of the reporting period. All form 13F-HR filings are based on the calendar year and are reported quarterly. If a date is not supplied, the most recent filing is returned. Submissions beginning 2013-06-30 are supported.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return. The number of previous filings to return. The date parameter takes priority over this parameter.

  *Exclusivos del proveedor `sec`:*

---
### Comando: `/equity/ownership/government_trades`

**Descripción:** Obtain government transaction data, including data from the Senate
and the House of Representatives.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None | list[str | None]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp.
  - `--chamber` (Opcional) `[Literal['house', 'senate', 'all'] | None]`: Government Chamber.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/equity/price/quote`

**Descripción:** Get the latest quote for a given stock. Quote includes price, volume, and other data.

- **Proveedores disponibles / soportados:** `cboe, fmp, intrinio, tmx, tradier, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): cboe, fmp, intrinio, tmx, tradier, yfinance.

  *Exclusivos del proveedor `cboe`:*
  - `--use_cache` (Opcional) `[bool | None]`: When True, the company directories will be cached for 24 hours and are used to validate symbols. The results of the function are not cached. Set as False to bypass.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `intrinio`:*
  - `--symbol` *(Requerido)* `[str]`: A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID).
  - `--source` (Opcional) `[Literal['iex', 'bats', 'bats_delayed', 'utp_delayed', 'cta_a_delayed', 'cta_b_delayed', 'intrinio_mx', 'intrinio_mx_plus', 'delayed_sip'] | None]`: Source of the data.

  *Exclusivos del proveedor `tmx`:*

  *Exclusivos del proveedor `tradier`:*

  *Exclusivos del proveedor `yfinance`:*

---
### Comando: `/equity/price/nbbo`

**Descripción:** Get the National Best Bid and Offer for a given stock.

- **Proveedores disponibles / soportados:** `polygon`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `polygon`:*
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return. Up to ten million records will be returned. Pagination occurs in groups of 50,000. Remaining limit values will always return 50,000 more records unless it is the last page. High volume tickers will require multiple max requests for a single day's NBBO records. Expect stocks, like SPY, to approach 1GB in size, per day, as a raw CSV. Splitting large requests into chunks is recommended for full-day requests of high-volume symbols.
  - `--date` (Opcional) `[date | None | str]`: A specific date to get data for. Use bracketed the timestamp parameters to specify exact time ranges.
  - `--timestamp_lt` (Opcional) `[datetime | str | None]`: Query by datetime, less than. Either a date with the format 'YYYY-MM-DD' or a TZ-aware timestamp string, 'YYYY-MM-DDTH:M:S.000000000-04:00'. Include all nanoseconds and the 'T' between the day and hour.
  - `--timestamp_gt` (Opcional) `[datetime | str | None]`: Query by datetime, greater than. Either a date with the format 'YYYY-MM-DD' or a TZ-aware timestamp string, 'YYYY-MM-DDTH:M:S.000000000-04:00'. Include all nanoseconds and the 'T' between the day and hour.
  - `--timestamp_lte` (Opcional) `[datetime | str | None]`: Query by datetime, less than or equal to. Either a date with the format 'YYYY-MM-DD' or a TZ-aware timestamp string, 'YYYY-MM-DDTH:M:S.000000000-04:00'. Include all nanoseconds and the 'T' between the day and hour.
  - `--timestamp_gte` (Opcional) `[datetime | str | None]`: Query by datetime, greater than or equal to. Either a date with the format 'YYYY-MM-DD' or a TZ-aware timestamp string, 'YYYY-MM-DDTH:M:S.000000000-04:00'. Include all nanoseconds and the 'T' between the day and hour.

---
### Comando: `/equity/price/historical`

**Descripción:** Get historical price data for a given stock. This includes open, high, low, close, and volume.

- **Proveedores disponibles / soportados:** `alpha_vantage, cboe, fmp, intrinio, polygon, tiingo, tmx, tradier, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): alpha_vantage, cboe, fmp, polygon, tiingo, tmx, tradier, yfinance.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `alpha_vantage`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '15m', '30m', '60m', '1d', '1W', '1M'] | None]`: Time interval of the data to return.
  - `--adjustment` (Opcional) `[Literal['splits_only', 'splits_and_dividends', 'unadjusted'] | None]`: The adjustment factor to apply. 'splits_only' is not supported for intraday data.
  - `--extended_hours` (Opcional) `[bool | None]`: Include Pre and Post market data.

  *Exclusivos del proveedor `cboe`:*
  - `--interval` (Opcional) `[Literal['1m', '1d'] | None]`: Time interval of the data to return. The most recent trading day is not including in daily historical data. Intraday data is only available for the most recent trading day at 1 minute intervals.
  - `--use_cache` (Opcional) `[bool | None]`: When True, the company directories will be cached for 24 hours and are used to validate symbols. The results of the function are not cached. Set as False to bypass.

  *Exclusivos del proveedor `fmp`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '15m', '30m', '1h', '4h', '1d'] | None]`: Time interval of the data to return.
  - `--adjustment` (Opcional) `[Literal['splits_only', 'splits_and_dividends', 'unadjusted'] | None]`: Type of adjustment for historical prices. Only applies to daily data.

  *Exclusivos del proveedor `intrinio`:*
  - `--symbol` *(Requerido)* `[str]`: A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID).
  - `--interval` (Opcional) `[Literal['1m', '5m', '10m', '15m', '30m', '60m', '1h', '1d', '1W', '1M', '1Q', '1Y'] | None]`: Time interval of the data to return.
  - `--start_time` (Opcional) `[datetime.time | None]`: Return intervals starting at the specified time on the `start_date` formatted as 'HH:MM:SS'.
  - `--end_time` (Opcional) `[datetime.time | None]`: Return intervals stopping at the specified time on the `end_date` formatted as 'HH:MM:SS'.
  - `--timezone` (Opcional) `[str | None]`: Timezone of the data, in the IANA format (Continent/City).
  - `--source` (Opcional) `[Literal['realtime', 'delayed', 'nasdaq_basic'] | None]`: The source of the data.

  *Exclusivos del proveedor `polygon`:*
  - `--interval` (Opcional) `[str | None]`: Time interval of the data to return. The numeric portion of the interval can be any positive integer. The letter portion can be one of the following: s, m, h, d, W, M, Q, Y
  - `--adjustment` (Opcional) `[Literal['splits_only', 'unadjusted'] | None]`: The adjustment factor to apply. Default is splits only.
  - `--extended_hours` (Opcional) `[bool | None]`: Include Pre and Post market data.
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order of the data. This impacts the results in combination with the 'limit' parameter. The results are always returned in ascending order by date.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `tiingo`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '15m', '30m', '90m', '1h', '2h', '4h', '1d', '1W', '1M', '1Y'] | None]`: Time interval of the data to return.

  *Exclusivos del proveedor `tmx`:*
  - `--interval` (Opcional) `[Literal['1m', '2m', '5m', '15m', '30m', '60m', '1h', '1d', '1W', '1M'] | None]`: Time interval of the data to return. Or, any integer (entered as a string) representing the number of minutes. Default is daily data. There is no extended hours data, and intraday data is limited to after April 12 2022.
  - `--adjustment` (Opcional) `[Literal['splits_only', 'splits_and_dividends', 'unadjusted'] | None]`: The adjustment factor to apply. Only valid for daily data.

  *Exclusivos del proveedor `tradier`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '15m', '1d', '1W', '1M'] | None]`: Time interval of the data to return.
  - `--extended_hours` (Opcional) `[bool | None]`: Include Pre and Post market data.

  *Exclusivos del proveedor `yfinance`:*
  - `--interval` (Opcional) `[Literal['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1W', '1M', '1Q'] | None]`: Time interval of the data to return.
  - `--extended_hours` (Opcional) `[bool | None]`: Include Pre and Post market data.
  - `--include_actions` (Opcional) `[bool | None]`: Include dividends and stock splits in results.
  - `--adjustment` (Opcional) `[Literal['splits_only', 'splits_and_dividends'] | None]`: The adjustment factor to apply. Default is splits only.

---
### Comando: `/equity/price/performance`

**Descripción:** Get price performance data for a given stock. This includes price changes for different time periods.

- **Proveedores disponibles / soportados:** `finviz, fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): finviz, fmp.

  *Exclusivos del proveedor `finviz`:*

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/equity/shorts/fails_to_deliver`

**Descripción:** Get reported Fail-to-deliver (FTD) data.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `sec`:*
  - `--limit` (Opcional) `[int | None]`: Limit the number of reports to parse, from most recent.         Approximately 24 reports per year, going back to 2009.
  - `--skip_reports` (Opcional) `[int | None]`: Skip N number of reports from current. A value of 1 will skip the most recent report.
  - `--use_cache` (Opcional) `[bool | None]`: Whether or not to use cache for the request, default is True. Each reporting period is a separate URL, new reports will be added to the cache.

---
### Comando: `/equity/shorts/short_volume`

**Descripción:** Get reported Fail-to-deliver (FTD) data.

- **Proveedores disponibles / soportados:** `stockgrid`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `stockgrid`:*

---
### Comando: `/equity/shorts/short_interest`

**Descripción:** Get reported short volume and days to cover data.

- **Proveedores disponibles / soportados:** `finra`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `finra`:*

---
### Comando: `/equity/search`

**Descripción:** Search for stock symbol, CIK, LEI, or company name.

- **Proveedores disponibles / soportados:** `cboe, intrinio, nasdaq, sec, tmx, tradier`

**Flags / Parámetros (Standard & Providers):**
  - `--query` (Opcional) `[str | None]`: Search query.
  - `--is_symbol` (Opcional) `[bool | None]`: Whether to search by ticker symbol.

  *Exclusivos del proveedor `cboe`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use the cache or not.

  *Exclusivos del proveedor `intrinio`:*
  - `--active` (Opcional) `[bool | None]`: When true, return companies that are actively traded (having stock prices within the past 14 days). When false, return companies that are not actively traded or never have been traded.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `nasdaq`:*
  - `--is_etf` (Opcional) `[bool | None]`: If True, returns only ETFs.

  *Exclusivos del proveedor `sec`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use the cache or not.
  - `--is_fund` (Opcional) `[bool | None]`: Whether to direct the search to the list of mutual funds and ETFs.

  *Exclusivos del proveedor `tmx`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use a cached request. The list of companies is cached for two days.

  *Exclusivos del proveedor `tradier`:*
  - `--is_symbol` (Opcional) `[bool | None]`: Whether the query is a symbol. Defaults to False.

---
### Comando: `/equity/screener`

**Descripción:** Screen for companies meeting various criteria.

These criteria include market cap, price, beta, volume, and dividend yield.

- **Proveedores disponibles / soportados:** `finviz, fmp, nasdaq, yfinance`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `finviz`:*
  - `--metric` (Opcional) `[Literal['overview', 'valuation', 'financial', 'ownership', 'performance', 'technical'] | None]`: The data group to return, default is 'overview'.
  - `--exchange` (Opcional) `[Literal['all', 'amex', 'nasdaq', 'nyse'] | None]`: Filter by exchange.
  - `--index` (Opcional) `[Literal['all', 'dow', 'nasdaq', 'sp500', 'russell'] | None]`: Filter by index.
  - `--sector` (Opcional) `[Literal['all', 'energy', 'materials', 'industrials', 'consumer_cyclical', 'consumer_defensive', 'financial', 'healthcare', 'technology', 'communication_services', 'utilities', 'real_estate'] | None]`: Filter by sector.
  - `--industry` (Opcional) `[str | None]`: Filter by industry.
  - `--mktcap` (Opcional) `[Literal['all', 'mega', 'large', 'large_over', 'large_under', 'mid', 'mid_over', 'mid_under', 'small', 'small_over', 'small_under', 'micro', 'micro_over', 'micro_under', 'nano'] | None]`: Filter by market cap.     Mega - > 200B     Large - 10B - 200B     Mid - 2B - 10B     Small - 300M - 2B     Micro - 50M - 300M     Nano - < 50M
  - `--recommendation` (Opcional) `[Literal['all', 'strong_buy', 'buy+', 'buy', 'hold+', 'hold', 'hold-', 'sell', 'sell-', 'strong_sell'] | None]`: Filter by analyst recommendation.
  - `--signal` (Opcional) `[str | None]`: The Finviz screener signal to use. When no parameters are provided, the screener defaults to 'top_gainers'. Available signals are:         channel: both support and resistance trendlines are horizontal         channel_down: both support and resistance trendlines slope downward         channel_up: both support and resistance trendlines slope upward         double_bottom: stock with 'W' shape that indicates a bullish reversal in trend         double_top: stock with 'M' shape that indicates a bearish reversal in trend         downgrades: stocks downgraded by analysts today         earnings_after: companies reporting earnings today, after market close         earnings_before: companies reporting earnings today, before market open         head_shoulders: chart formation that predicts a bullish-to-bearish trend reversal         head_shoulders_inverse: chart formation that predicts a bearish-to-bullish trend reversal         horizontal_sr: horizontal channel of price range between support and resistance trendlines         major_news: stocks with the highest news coverage today         most_active: stocks with the highest trading volume today         most_volatile: stocks with the highest widest high/low trading range today         multiple_bottom: same as double_bottom hitting more lows         multiple_top: same as double_top hitting more highs         new_high: stocks making 52-week high today         new_low: stocks making 52-week low today         overbought: stock is becoming overvalued and may experience a pullback.         oversold: oversold stocks may represent a buying opportunity for investors         recent_insider_buying: stocks with recent insider buying activity         recent_insider_selling: stocks with recent insider selling activity         tl_resistance: once a rising trendline is broken         tl_support: once a falling trendline is broken         top_gainers: stocks with the highest price gain percent today         top_losers: stocks with the highest price percent loss today         triangle_ascending: upward trendline support and horizontal trendline resistance         triangle_descending: horizontal trendline support and downward trendline resistance         unusual_volume: stocks with unusually high volume today - the highest relative volume ratio         upgrades: stocks upgraded by analysts today         wedge: upward trendline support, downward trendline resistance (contiunation)         wedge_down: downward trendline support and downward trendline resistance (reversal)         wedge_up: upward trendline support and upward trendline resistance (reversal)
  - `--preset` (Opcional) `[str | None]`: A configured preset file to use for the query. This overrides all other query parameters except 'metric', and 'limit'. Presets (.ini text files) can be created and modified in the '~/OpenBBUserData/finviz/presets' directory. If the path does not exist, it will be created and populated with the default presets on the first run. Refer to the file, 'screener_template.ini', for the format and options.  Note: Syntax of parameters in preset files must follow the template file exactly  - i.e, Analyst Recom. = Strong Buy (1)
  - `--filters_dict` (Opcional) `[dict | str | None]`: A formatted dictionary, or serialized JSON string, of additional filters to apply to the query. This parameter can be used as an alternative to preset files, and is ignored when a preset is supplied. Invalid entries will raise an error. Syntax should follow the 'screener_template.ini' file.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `fmp`:*
  - `--mktcap_min` (Opcional) `[int | None]`: Filter by market cap greater than this value.
  - `--mktcap_max` (Opcional) `[int | None]`: Filter by market cap less than this value.
  - `--price_min` (Opcional) `[float | None]`: Filter by price greater than this value.
  - `--price_max` (Opcional) `[float | None]`: Filter by price less than this value.
  - `--beta_min` (Opcional) `[float | None]`: Filter by a beta greater than this value.
  - `--beta_max` (Opcional) `[float | None]`: Filter by a beta less than this value.
  - `--volume_min` (Opcional) `[int | None]`: Filter by volume greater than this value.
  - `--volume_max` (Opcional) `[int | None]`: Filter by volume less than this value.
  - `--dividend_min` (Opcional) `[float | None]`: Filter by dividend amount greater than this value.
  - `--dividend_max` (Opcional) `[float | None]`: Filter by dividend amount less than this value.
  - `--sector` (Opcional) `[Literal['consumer_cyclical', 'energy', 'technology', 'industrials', 'financial_services', 'basic_materials', 'communication_services', 'consumer_defensive', 'healthcare', 'real_estate', 'utilities', 'industrial_goods', 'financial', 'services'] | None]`: Filter by sector.
  - `--industry` (Opcional) `[str | None]`: Filter by industry.
  - `--country` (Opcional) `[Literal['ae', 'ai', 'ar', 'at', 'au', 'ax', 'az', 'bb', 'bd', 'be', 'bg', 'bh', 'bm', 'br', 'bs', 'bw', 'ca', 'ch', 'ci', 'ck', 'cl', 'cn', 'co', 'cr', 'cw', 'cy', 'cz', 'de', 'dk', 'do', 'ee', 'eg', 'es', 'fi', 'fk', 'fr', 'ga', 'gb', 'ge', 'gf', 'gg', 'gi', 'gl', 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'im', 'in', 'is', 'it', 'je', 'jo', 'jp', 'ke', 'kg', 'kh', 'kr', 'kw', 'ky', 'kz', 'li', 'lt', 'lu', 'lv', 'ma', 'mc', 'me', 'mk', 'mm', 'mn', 'mo', 'mq', 'mt', 'mu', 'mx', 'my', 'mz', 'na', 'ng', 'nl', 'no', 'nz', 'pa', 'pe', 'pg', 'ph', 'pk', 'pl', 'pr', 'pt', 'qa', 're', 'ro', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'sn', 'sr', 'tc', 'th', 'tr', 'tw', 'tz', 'ua', 'uk', 'us', 'uy', 'vg', 'vn', 'za', 'zm'] | None]`: Filter by country, as a two-letter country code.
  - `--exchange` (Opcional) `[Literal['amex', 'ams', 'ase', 'asx', 'ath', 'bme', 'bru', 'bud', 'bue', 'cai', 'cnq', 'cph', 'dfm', 'doh', 'etf', 'euronext', 'hel', 'hkse', 'ice', 'iob', 'ist', 'jkt', 'jnb', 'jpx', 'kls', 'koe', 'ksc', 'kuw', 'lse', 'mex', 'nasdaq', 'neo', 'nse', 'nyse', 'nze', 'osl', 'otc', 'pnk', 'pra', 'ris', 'sao', 'sau', 'set', 'sgo', 'shh', 'shz', 'six', 'sto', 'tai', 'tlv', 'tsx', 'two', 'vie', 'wse', 'xetra'] | None]`: Filter by exchange.
  - `--is_etf` (Opcional) `[bool | None]`: If true, includes ETFs.
  - `--is_active` (Opcional) `[bool | None]`: If false, returns only inactive tickers.
  - `--is_fund` (Opcional) `[bool | None]`: If true, includes funds.
  - `--all_share_classes` (Opcional) `[bool | None]`: If true, includes all share classes of a equity.
  - `--limit` (Opcional) `[int | None]`: Limit the number of results to return.

  *Exclusivos del proveedor `nasdaq`:*
  - `--exchange` (Opcional) `[Literal['all', 'nasdaq', 'nyse', 'amex'] | None]`: Filter by exchange.
  - `--exsubcategory` (Opcional) `[Literal['all', 'ngs', 'ngm', 'ncm', 'adr'] | None]`: Filter by exchange subcategory.     NGS - Nasdaq Global Select Market     NGM - Nasdaq Global Market     NCM - Nasdaq Capital Market     ADR - American Depository Receipt
  - `--mktcap` (Opcional) `[Literal['all', 'mega', 'large', 'mid', 'small', 'micro'] | None]`: Filter by market cap.     Mega - > 200B     Large - 10B - 200B     Mid - 2B - 10B     Small - 300M - 2B     Micro - 50M - 300M
  - `--recommendation` (Opcional) `[Literal['all', 'strong_buy', 'buy', 'hold', 'sell', 'strong_sell'] | None]`: Filter by consensus analyst action.
  - `--sector` (Opcional) `[Literal['all', 'energy', 'basic_materials', 'industrials', 'consumer_staples', 'consumer_discretionary', 'health_care', 'financial_services', 'technology', 'communication_services', 'utilities', 'real_estate'] | None]`: Filter by sector.
  - `--region` (Opcional) `[Literal['all', 'africa', 'asia', 'australia_and_south_pacific', 'caribbean', 'europe', 'middle_east', 'north_america', 'south_america'] | None]`: Filter by region.
  - `--country` (Opcional) `[Literal['all', 'argentina', 'armenia', 'australia', 'austria', 'belgium', 'bermuda', 'brazil', 'canada', 'cayman_islands', 'chile', 'colombia', 'costa_rica', 'curacao', 'cyprus', 'denmark', 'finland', 'france', 'germany', 'greece', 'guernsey', 'hong_kong', 'india', 'indonesia', 'ireland', 'isle_of_man', 'israel', 'italy', 'japan', 'jersey', 'luxembourg', 'macau', 'mexico', 'monaco', 'netherlands', 'norway', 'panama', 'peru', 'philippines', 'puerto_rico', 'russia', 'singapore', 'south_africa', 'south_korea', 'spain', 'sweden', 'switzerland', 'taiwan', 'turkey', 'united_kingdom', 'united_states', 'usa'] | None]`: Filter by country.
  - `--limit` (Opcional) `[int | None]`: Limit the number of results to return.

  *Exclusivos del proveedor `yfinance`:*
  - `--country` (Opcional) `[str | None]`: Filter by country, as a two-letter country code. Default is, 'us'. Use, 'all', for all countries.
  - `--exchange` (Opcional) `[Literal['ams', 'aqs', 'ase', 'asx', 'ath', 'ber', 'bru', 'bse', 'bts', 'bud', 'bue', 'bvb', 'bvc', 'ccs', 'cnq', 'cph', 'cxe', 'dfm', 'doh', 'dus', 'ebs', 'fka', 'fra', 'ger', 'ham', 'han', 'hel', 'hkg', 'ice', 'iob', 'ise', 'ist', 'jkt', 'jnb', 'jpx', 'kls', 'kuw', 'lis', 'lit', 'lse', 'mce', 'mex', 'mil', 'mun', 'ncm', 'neo', 'ngm', 'nms', 'nsi', 'nyq', 'nze', 'oem', 'oqb', 'oqx', 'osl', 'par', 'pnk', 'pra', 'ris', 'sau', 'ses', 'set', 'sgo', 'shh', 'shz', 'sto', 'stu', 'tai', 'tal', 'tlv', 'tor', 'two', 'van', 'vie', 'vse', 'wse'] | None]`: Filter by exchange.
  - `--sector` (Opcional) `[Literal['basic_materials', 'communication_services', 'consumer_cyclical', 'consumer_defensive', 'energy', 'financial_services', 'healthcare', 'industrials', 'real_estate', 'technology', 'utilities'] | None]`: Filter by sector.
  - `--industry` (Opcional) `[str | None]`: Filter by industry.
  - `--mktcap_min` (Opcional) `[int | None]`: Filter by market cap greater than this value. Default is 500M.
  - `--mktcap_max` (Opcional) `[int | None]`: Filter by market cap less than this value.
  - `--price_min` (Opcional) `[float | None]`: Filter by price greater than this value. Default is, 5
  - `--price_max` (Opcional) `[float | None]`: Filter by price less than this value.
  - `--volume_min` (Opcional) `[int | None]`: Filter by volume greater than this value. Default is, 10K
  - `--volume_max` (Opcional) `[int | None]`: Filter by volume less than this value.
  - `--beta_min` (Opcional) `[float | None]`: Filter by a beta greater than this value.
  - `--beta_max` (Opcional) `[float | None]`: Filter by a beta less than this value.
  - `--limit` (Opcional) `[int | None]`: Limit the number of results returned. Default is, 200. Set to, 0, for all results.

---
### Comando: `/equity/profile`

**Descripción:** Get general information about a company. This includes company name, industry, sector and price data.

- **Proveedores disponibles / soportados:** `finviz, fmp, intrinio, tmx, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): finviz, fmp, intrinio, tmx, yfinance.

  *Exclusivos del proveedor `finviz`:*

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `intrinio`:*

  *Exclusivos del proveedor `tmx`:*

  *Exclusivos del proveedor `yfinance`:*

---
### Comando: `/equity/market_snapshots`

**Descripción:** Get an updated equity market snapshot. This includes price data for thousands of stocks.

- **Proveedores disponibles / soportados:** `fmp, intrinio, polygon`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `fmp`:*
  - `--market` (Opcional) `[Literal['amex', 'ams', 'ase', 'asx', 'ath', 'bme', 'bru', 'bud', 'bue', 'cai', 'cnq', 'commodity', 'cph', 'crypto', 'dfm', 'doh', 'dus', 'etf', 'euronext', 'forex', 'hel', 'hkse', 'ice', 'iob', 'index', 'ist', 'jkt', 'jnb', 'jpx', 'kls', 'koe', 'ksc', 'kuw', 'lse', 'mex', 'mil', 'mutual_fund', 'nasdaq', 'neo', 'nse', 'nyse', 'nze', 'osl', 'otc', 'pnk', 'pra', 'ris', 'sao', 'sau', 'ses', 'set', 'sgo', 'shh', 'shz', 'six', 'sto', 'tai', 'tlv', 'tsx', 'two', 'vie', 'wse', 'xetra'] | None]`: The market to fetch data for.

  *Exclusivos del proveedor `intrinio`:*
  - `--date` (Opcional) `[date | datetime | str | None | str]`: The date of the data. Can be a datetime or an ISO datetime string. Historical data appears to go back to mid-June 2022. Example: '2024-03-08T12:15:00+0400'

  *Exclusivos del proveedor `polygon`:*

---
### Comando: `/equity/historical_market_cap`

**Descripción:** Get the historical market cap of a ticker symbol.

- **Proveedores disponibles / soportados:** `fmp, intrinio`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp, intrinio.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `intrinio`:*
  - `--interval` (Opcional) `[Literal['day', 'week', 'month', 'quarter', 'year'] | None]`: None

---
### Comando: `/etf/discovery/gainers`

**Descripción:** Get the top ETF gainers.

- **Proveedores disponibles / soportados:** `wsj`

**Flags / Parámetros (Standard & Providers):**
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `wsj`:*

---
### Comando: `/etf/discovery/losers`

**Descripción:** Get the top ETF losers.

- **Proveedores disponibles / soportados:** `wsj`

**Flags / Parámetros (Standard & Providers):**
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `wsj`:*

---
### Comando: `/etf/discovery/active`

**Descripción:** Get the most active ETFs.

- **Proveedores disponibles / soportados:** `wsj`

**Flags / Parámetros (Standard & Providers):**
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `wsj`:*

---
### Comando: `/etf/search`

**Descripción:** Search for ETFs.

An empty query returns the full list of ETFs from the provider.

- **Proveedores disponibles / soportados:** `fmp, intrinio, tmx`

**Flags / Parámetros (Standard & Providers):**
  - `--query` (Opcional) `[str | None]`: Search query.

  *Exclusivos del proveedor `fmp`:*
  - `--exchange` (Opcional) `[Literal['amex', 'nyse', 'nasdaq', 'tsx', 'euronext'] | None]`: Exchange where the ETF is listed. If not provided, all exchanges are searched.

  *Exclusivos del proveedor `intrinio`:*
  - `--exchange` (Opcional) `[Literal['xnas', 'arcx', 'bats', 'xnys', 'bvmf', 'xshg', 'xshe', 'xhkg', 'xbom', 'xnse', 'xidx', 'tase', 'xkrx', 'xkls', 'xmex', 'xses', 'roco', 'xtai', 'xbkk', 'xist'] | None]`: Target a specific exchange by providing the MIC code.

  *Exclusivos del proveedor `tmx`:*
  - `--div_freq` (Opcional) `[Literal['monthly', 'annually', 'quarterly'] | None]`: The dividend payment frequency.
  - `--sort_by` (Opcional) `[Literal['aum', 'return_1m', 'return_3m', 'return_6m', 'return_1y', 'return_3y', 'return_ytd', 'beta_1y', 'volume_avg_daily', 'management_fee', 'distribution_yield', 'pb_ratio', 'pe_ratio'] | None]`: The column to sort by.
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use a cached request. All ETF data comes from a single JSON file that is updated daily. To bypass, set to False. If True, the data will be cached for 4 hours.

---
### Comando: `/etf/historical`

**Descripción:** ETF Historical Market Price.

- **Proveedores disponibles / soportados:** `alpha_vantage, cboe, fmp, intrinio, polygon, tiingo, tmx, tradier, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): alpha_vantage, cboe, fmp, polygon, tiingo, tmx, tradier, yfinance.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `alpha_vantage`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '15m', '30m', '60m', '1d', '1W', '1M'] | None]`: Time interval of the data to return.
  - `--adjustment` (Opcional) `[Literal['splits_only', 'splits_and_dividends', 'unadjusted'] | None]`: The adjustment factor to apply. 'splits_only' is not supported for intraday data.
  - `--extended_hours` (Opcional) `[bool | None]`: Include Pre and Post market data.

  *Exclusivos del proveedor `cboe`:*
  - `--interval` (Opcional) `[Literal['1m', '1d'] | None]`: Time interval of the data to return. The most recent trading day is not including in daily historical data. Intraday data is only available for the most recent trading day at 1 minute intervals.
  - `--use_cache` (Opcional) `[bool | None]`: When True, the company directories will be cached for 24 hours and are used to validate symbols. The results of the function are not cached. Set as False to bypass.

  *Exclusivos del proveedor `fmp`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '15m', '30m', '1h', '4h', '1d'] | None]`: Time interval of the data to return.
  - `--adjustment` (Opcional) `[Literal['splits_only', 'splits_and_dividends', 'unadjusted'] | None]`: Type of adjustment for historical prices. Only applies to daily data.

  *Exclusivos del proveedor `intrinio`:*
  - `--symbol` *(Requerido)* `[str]`: A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID).
  - `--interval` (Opcional) `[Literal['1m', '5m', '10m', '15m', '30m', '60m', '1h', '1d', '1W', '1M', '1Q', '1Y'] | None]`: Time interval of the data to return.
  - `--start_time` (Opcional) `[datetime.time | None]`: Return intervals starting at the specified time on the `start_date` formatted as 'HH:MM:SS'.
  - `--end_time` (Opcional) `[datetime.time | None]`: Return intervals stopping at the specified time on the `end_date` formatted as 'HH:MM:SS'.
  - `--timezone` (Opcional) `[str | None]`: Timezone of the data, in the IANA format (Continent/City).
  - `--source` (Opcional) `[Literal['realtime', 'delayed', 'nasdaq_basic'] | None]`: The source of the data.

  *Exclusivos del proveedor `polygon`:*
  - `--interval` (Opcional) `[str | None]`: Time interval of the data to return. The numeric portion of the interval can be any positive integer. The letter portion can be one of the following: s, m, h, d, W, M, Q, Y
  - `--adjustment` (Opcional) `[Literal['splits_only', 'unadjusted'] | None]`: The adjustment factor to apply. Default is splits only.
  - `--extended_hours` (Opcional) `[bool | None]`: Include Pre and Post market data.
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order of the data. This impacts the results in combination with the 'limit' parameter. The results are always returned in ascending order by date.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `tiingo`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '15m', '30m', '90m', '1h', '2h', '4h', '1d', '1W', '1M', '1Y'] | None]`: Time interval of the data to return.

  *Exclusivos del proveedor `tmx`:*
  - `--interval` (Opcional) `[Literal['1m', '2m', '5m', '15m', '30m', '60m', '1h', '1d', '1W', '1M'] | None]`: Time interval of the data to return. Or, any integer (entered as a string) representing the number of minutes. Default is daily data. There is no extended hours data, and intraday data is limited to after April 12 2022.
  - `--adjustment` (Opcional) `[Literal['splits_only', 'splits_and_dividends', 'unadjusted'] | None]`: The adjustment factor to apply. Only valid for daily data.

  *Exclusivos del proveedor `tradier`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '15m', '1d', '1W', '1M'] | None]`: Time interval of the data to return.
  - `--extended_hours` (Opcional) `[bool | None]`: Include Pre and Post market data.

  *Exclusivos del proveedor `yfinance`:*
  - `--interval` (Opcional) `[Literal['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1W', '1M', '1Q'] | None]`: Time interval of the data to return.
  - `--extended_hours` (Opcional) `[bool | None]`: Include Pre and Post market data.
  - `--include_actions` (Opcional) `[bool | None]`: Include dividends and stock splits in results.
  - `--adjustment` (Opcional) `[Literal['splits_only', 'splits_and_dividends'] | None]`: The adjustment factor to apply. Default is splits only.

---
### Comando: `/etf/info`

**Descripción:** ETF Information Overview.

- **Proveedores disponibles / soportados:** `fmp, intrinio, tmx, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. (ETF) Multiple items allowed for provider(s): fmp, intrinio, tmx, yfinance.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `intrinio`:*

  *Exclusivos del proveedor `tmx`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use a cached request. All ETF data comes from a single JSON file that is updated daily. To bypass, set to False. If True, the data will be cached for 4 hours.

  *Exclusivos del proveedor `yfinance`:*

---
### Comando: `/etf/sectors`

**Descripción:** ETF Sector weighting.

- **Proveedores disponibles / soportados:** `fmp, tmx`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. (ETF) Multiple items allowed for provider(s): fmp, tmx.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `tmx`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use a cached request. All ETF data comes from a single JSON file that is updated daily. To bypass, set to False. If True, the data will be cached for 4 hours.

---
### Comando: `/etf/countries`

**Descripción:** ETF Country weighting.

- **Proveedores disponibles / soportados:** `fmp, tmx`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): fmp, tmx.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `tmx`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use a cached request. All ETF data comes from a single JSON file that is updated daily. To bypass, set to False. If True, the data will be cached for 4 hours.

---
### Comando: `/etf/price_performance`

**Descripción:** Price performance as a return, over different periods.

- **Proveedores disponibles / soportados:** `finviz, fmp, intrinio`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): finviz, fmp, intrinio.

  *Exclusivos del proveedor `finviz`:*

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `intrinio`:*
  - `--return_type` (Opcional) `[Literal['trailing', 'calendar'] | None]`: The type of returns to return, a trailing or calendar window.
  - `--adjustment` (Opcional) `[Literal['splits_only', 'splits_and_dividends'] | None]`: The adjustment factor, 'splits_only' will return pure price performance.

---
### Comando: `/etf/holdings`

**Descripción:** Get the holdings for an individual ETF.

- **Proveedores disponibles / soportados:** `fmp, intrinio, tmx`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for. (ETF)

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `intrinio`:*
  - `--date` (Opcional) `[date | None | str]`: A specific date to get data for.

  *Exclusivos del proveedor `tmx`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use a cached request. All ETF data comes from a single JSON file that is updated daily. To bypass, set to False. If True, the data will be cached for 4 hours.

---
### Comando: `/etf/nport_disclosure`

**Descripción:** Get SEC NPORT-P disclosure filings for a given ETF or mutual fund (US only).

- **Proveedores disponibles / soportados:** `fmp, sec`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for. (Fund ticker or CIK)
  - `--year` (Opcional) `[int | None]`: Reporting year of the filing. Default is the year for the most recent, reported, quarter.
  - `--quarter` (Opcional) `[int | None]`: Reporting quarter of the filing. Default is the most recent, reported, quarter.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `sec`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether or not to use cache for the request.

---
### Comando: `/etf/equity_exposure`

**Descripción:** Get the exposure to ETFs for a specific stock.

- **Proveedores disponibles / soportados:** `fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. (underlying equity) Multiple items allowed for provider(s): fmp.

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/famafrench/factors`

**Descripción:** Fama-French factors.

Metadata for the selected dataset are returned in the
`extra['results_metadata']` field of the response.

Source
------

https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html

All returns are in U.S. dollars, include dividends and capital gains,
and are not continuously compounded.

Market is the return on a region's value-weight market portfolio
minus the U.S. one month T-bill rate.

The Fama/French 5 factors (2x3) are constructed using the 6,
value-weight, portfolios formed on size and book-to-market, the 6,
value-weight, portfolios formed on size and operating profitability,
and the 6, value-weight, portfolios formed on size and investment.

To construct the SMB, HML, RMW, and CMA factors, we sort stocks in a
region into two market cap and three respective book-to-market equity (B/M),
operating profitability (OP), and investment (INV) groups at the end of each June.

Big stocks are those in the top 90% of June market cap for the region,
and small stocks are those in the bottom 10%.
The B/M, OP, and INV breakpoints for a region are the 30th and 70th percentiles
of respective ratios for the big stocks of the region.

Rm–Rf for July of year t to June of t+1 include all stocks
for which we have market equity data for June of t.
SMB, HML, RMW, and CMA for July of year t to June of t+1 include all stocks
for which we have market equity data for December of t-1
and June of t, (positive) book equity data for t-1 (for SMB, HML, and RMW),
non-missing revenues and at least one of the following: cost of goods sold,
selling, general and administrative expenses, or interest expense for
t-1 (for SMB and RMW), and total assets data for t-2 and t-1 (for SMB and CMA).

The momentum and short term reversal portfolios are reconstituted monthly
and the other research portfolios are reconstituted annually.
We reconstruct the full history of returns each month when we update the portfolios.

- **Proveedores disponibles / soportados:** `famafrench`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `famafrench`:*
  - `--region` (Opcional) `[Literal['america', 'north_america', 'europe', 'japan', 'asia_pacific_ex_japan', 'developed', 'developed_ex_us', 'emerging'] | None]`: Region of focus. Default is America.
  - `--factor` (Opcional) `[Literal['5_factors', '3_factors', 'momentum', 'st_reversal', 'lt_reversal'] | None]`: Factor to fetch. Default is the 3-Factor Model.Short/long-term reversals are available only for America.
  - `--frequency` (Opcional) `[Literal['daily', 'weekly', 'monthly', 'annual'] | None]`: Frequency of the factor data.Not all are available for all regions, and intervals depend on the factor selected. Weekly is only available for the US 3-Factor Model.
  - `--start_date` (Opcional) `[date | None]`: Start date of the data. Defaults to the complete data range.
  - `--end_date` (Opcional) `[date | None]`: End date of the data. Defaults to the complete data range.

---
### Comando: `/famafrench/us_portfolio_returns`

**Descripción:** US Portfolio returns.

Metadata for the selected dataset are returned in the
`extra['results_metadata']` field of the response.

Source
------

https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html

All returns are in U.S. dollars, include dividends (unless the portfolio is 'wout_div')
and capital gains, and are not continuously compounded.


The momentum and short term reversal portfolios are reconstituted monthly
and the other research portfolios are reconstituted annually.
We reconstruct the full history of returns each month when we update the portfolios.


Size and Book-to-Market Portfolios
----------------------------------

- Small Value
- Small Neutral
- Small Growth
- Big Value
- Big Neutral
- Big Growth

BE < 0; bottom 30%, middle 40%, top 30%; quintiles; deciles.
Firms with negative book equity are in only the BE < 0 portfolio.

Size and Operating Profitability Portfolios
-------------------------------------------

- Small Robust
- Small Neutral
- Small Weak
- Big Robust
- Big Neutral
- Big Weak

Operating Profitability bottom 30%, middle 40%, top 30%; quintiles; deciles.

Size and Investment Portfolios
------------------------------

- Small Conservative
- Small Neutral
- Small Aggressive
- Big Conservative
- Big Neutral
- Big Aggressive

ME < 0 (not used); bottom 30%, middle 40%, top 30%; quintiles; deciles.
Investment bottom 30%, middle 40%, top 30%; quintiles; deciles.

Definitions
-----------

ME : Market Equity

Market equity (size) is price times shares outstanding.
Price and shares outstanding are from CRSP.

BE : Book Equity

Book equity is constructed from Compustat data or collected from the
Moody’s Industrial, Financial, and Utilities manuals.
BE is the book value of stockholders’ equity, plus balance sheet deferred taxes
and investment tax credit (if available), minus the book value of preferred stock.
Depending on availability, we use the redemption, liquidation, or par value (in that order)
to estimate the book value of preferred stock. Stockholders’ equity is the value reported
by Moody’s or Compustat, if it is available. If not, we measure stockholders’ equity as
the book value of common equity plus the par value of preferred stock,
or the book value of assets minus total liabilities (in that order).

See Davis, Fama, and French, 2000,
“Characteristics, Covariances, and Average Returns: 1929-1997”
Journal of Finance, for more details.

BE/ME : Book-to-Market

The book-to-market ratio used to form portfolios in June of year t is book equity
for the fiscal year ending in calendar year t-1,
divided by market equity at the end of December of t-1.

OP : Operating Profitability

The operating profitability ratio used to form portfolios in June of year t is annual revenues
minus cost of goods sold, interest expense, and selling, general, and administrative expense
divided by the sum of book equity and minority interest for the last fiscal year ending in t-1.

INV : Investment

The investment ratio used to form portfolios in June of year t is the change in total assets
from the fiscal year ending in year t-2 to the fiscal year ending in t-1,
divided by t-2 total assets.

E/P : Earnings/Price

Earnings is total earnings before extraordinary items, from Compustat.
The earnings/price ratio used to form portfolios in June of year t is earnings
for the fiscal year ending in calendar year t-1,
divided by market equity at the end of December of t-1.

CF/P : Cashflow/Price

Cashflow is total earnings before extraordinary items, plus equity’s share of depreciation,
plus deferred taxes (if available), from Compustat. Equity’s share is defined as market equity
divided by assets minus book equity plus market equity.
The cashflow/price ratio used to form portfolios in June of year t is the cashflow for the
fiscal year ending in calendar year t-1, divided by market equity at the end of December of t-1.

D/P : Dividend Yield

The dividend yield used to form portfolios in June of year t is the total dividends paid
from July of t-1 to June of t per dollar of equity in June of t.
The dividend yield is computed using the with and without dividend returns from CRSP,
as described in Fama and French, 1988, “Dividend yields and expected stock returns,”
Journal of Financial Economics 25.

- **Proveedores disponibles / soportados:** `famafrench`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `famafrench`:*
  - `--portfolio` (Opcional) `[Literal['portfolios_formed_on_me', 'portfolios_formed_on_me_wout_div', 'portfolios_formed_on_me_daily', 'portfolios_formed_on_be-me', 'portfolios_formed_on_be-me_wout_div', 'portfolios_formed_on_be-me_daily', 'portfolios_formed_on_op', 'portfolios_formed_on_op_wout_div', 'portfolios_formed_on_op_daily', 'portfolios_formed_on_inv', 'portfolios_formed_on_inv_wout_div', 'portfolios_formed_on_inv_daily', '6_portfolios_2x3', '6_portfolios_2x3_wout_div', '6_portfolios_2x3_weekly', '6_portfolios_2x3_daily', '25_portfolios_5x5', '25_portfolios_5x5_wout_div', '25_portfolios_5x5_daily', '100_portfolios_10x10', '100_portfolios_10x10_wout_div', '100_portfolios_10x10_daily', '6_portfolios_me_op_2x3', '6_portfolios_me_op_2x3_wout_div', '6_portfolios_me_op_2x3_daily', '25_portfolios_me_op_5x5', '25_portfolios_me_op_5x5_wout_div', '25_portfolios_me_op_5x5_daily', '100_portfolios_me_op_10x10', '100_portfolios_10x10_me_op_wout_div', '100_portfolios_me_op_10x10_daily', '6_portfolios_me_inv_2x3', '6_portfolios_me_inv_2x3_wout_div', '6_portfolios_me_inv_2x3_daily', '25_portfolios_me_inv_5x5', '25_portfolios_me_inv_5x5_wout_div', '25_portfolios_me_inv_5x5_daily', '100_portfolios_me_inv_10x10', '100_portfolios_10x10_me_inv_wout_div', '100_portfolios_me_inv_10x10_daily', '25_portfolios_beme_op_5x5', '25_portfolios_beme_op_5x5_wout_div', '25_portfolios_beme_op_5x5_daily', '25_portfolios_beme_inv_5x5', '25_portfolios_beme_inv_5x5_wout_div', '25_portfolios_beme_inv_5x5_daily', '25_portfolios_op_inv_5x5', '25_portfolios_op_inv_5x5_wout_div', '25_portfolios_op_inv_5x5_daily', '32_portfolios_me_beme_op_2x4x4', '32_portfolios_me_beme_op_2x4x4_wout_div', '32_portfolios_me_beme_inv_2x4x4', '32_portfolios_me_beme_inv_2x4x4_wout_div', '32_portfolios_me_op_inv_2x4x4', '32_portfolios_me_op_inv_2x4x4_wout_div', 'portfolios_formed_on_e-p', 'portfolios_formed_on_e-p_wout_div', 'portfolios_formed_on_cf-p', 'portfolios_formed_on_cf-p_wout_div', 'portfolios_formed_on_d-p', 'portfolios_formed_on_d-p_wout_div', '6_portfolios_me_ep_2x3', '6_portfolios_me_ep_2x3_wout_div', '6_portfolios_me_cfp_2x3', '6_portfolios_me_cfp_2x3_wout_div', '6_portfolios_me_dp_2x3', '6_portfolios_me_dp_2x3_wout_div', '6_portfolios_me_prior_12_2', '6_portfolios_me_prior_12_2_daily', '25_portfolios_me_prior_12_2', '25_portfolios_me_prior_12_2_daily', '10_portfolios_prior_12_2', '10_portfolios_prior_12_2_daily', '6_portfolios_me_prior_1_0', '6_portfolios_me_prior_1_0_daily', '25_portfolios_me_prior_1_0', '25_portfolios_me_prior_1_0_daily', '10_portfolios_prior_1_0', '10_portfolios_prior_1_0_daily', '6_portfolios_me_prior_60_13', '6_portfolios_me_prior_60_13_daily', '25_portfolios_me_prior_60_13', '25_portfolios_me_prior_60_13_daily', '10_portfolios_prior_60_13', '10_portfolios_prior_60_13_daily', 'portfolios_formed_on_ac', '25_portfolios_me_ac_5x5', 'portfolios_formed_on_beta', '25_portfolios_me_beta_5x5', 'portfolios_formed_on_ni', '25_portfolios_me_ni_5x5', 'portfolios_formed_on_var', '25_portfolios_me_var_5x5', 'portfolios_formed_on_resvar', '25_portfolios_me_resvar_5x5', '5_industry_portfolios', '5_industry_portfolios_wout_div', '5_industry_portfolios_daily', '10_industry_portfolios', '10_industry_portfolios_wout_div', '10_industry_portfolios_daily', '12_industry_portfolios', '12_industry_portfolios_wout_div', '12_industry_portfolios_daily', '17_industry_portfolios', '17_industry_portfolios_wout_div', '17_industry_portfolios_daily', '30_industry_portfolios', '30_industry_portfolios_wout_div', '30_industry_portfolios_daily', '38_industry_portfolios', '38_industry_portfolios_wout_div', '38_industry_portfolios_daily', '48_industry_portfolios', '48_industry_portfolios_wout_div', '48_industry_portfolios_daily', '49_industry_portfolios', '49_industry_portfolios_wout_div', '49_industry_portfolios_daily'] | None]`: The specific portfolio file to fetch.
  - `--measure` (Opcional) `[Literal['value', 'equal', 'number_of_firms', 'firm_size'] | None]`: The measure to fetch for the portfolio.
  - `--frequency` (Opcional) `[Literal['monthly', 'annual'] | None]`: The frequency of the data to fetch. Ignored if the portfolio ends with 'daily' or 'weekly'.
  - `--start_date` (Opcional) `[date | None | str]`: The start date for the data. Defaults to the earliest available date.
  - `--end_date` (Opcional) `[date | None | str]`: The end date for the data. Defaults to the latest available date.

---
### Comando: `/famafrench/regional_portfolio_returns`

**Descripción:** Regional portfolio returns.

Metadata for the selected dataset are returned in the
`extra['results_metadata']` field of the response.

See the `us_portfolio_returns` endpoint for more details.

- **Proveedores disponibles / soportados:** `famafrench`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `famafrench`:*
  - `--portfolio` (Opcional) `[Literal['asia_pacific_ex_japan_25_portfolios_me_be-me', 'asia_pacific_ex_japan_25_portfolios_me_be-me_daily', 'asia_pacific_ex_japan_25_portfolios_me_inv', 'asia_pacific_ex_japan_25_portfolios_me_inv_daily', 'asia_pacific_ex_japan_25_portfolios_me_op', 'asia_pacific_ex_japan_25_portfolios_me_op_daily', 'asia_pacific_ex_japan_25_portfolios_me_prior_12_2', 'asia_pacific_ex_japan_25_portfolios_me_prior_250_20_daily', 'asia_pacific_ex_japan_32_portfolios_me_be-me_inv_2x4x4', 'asia_pacific_ex_japan_32_portfolios_me_be-me_op_2x4x4', 'asia_pacific_ex_japan_32_portfolios_me_inv_op_2x4x4', 'asia_pacific_ex_japan_6_portfolios_me_be-me', 'asia_pacific_ex_japan_6_portfolios_me_be-me_daily', 'asia_pacific_ex_japan_6_portfolios_me_inv', 'asia_pacific_ex_japan_6_portfolios_me_inv_daily', 'asia_pacific_ex_japan_6_portfolios_me_op', 'asia_pacific_ex_japan_6_portfolios_me_op_daily', 'asia_pacific_ex_japan_6_portfolios_me_prior_12_2', 'asia_pacific_ex_japan_6_portfolios_me_prior_250_20_daily', 'developed_25_portfolios_me_be-me', 'developed_25_portfolios_me_be-me_daily', 'developed_25_portfolios_me_inv', 'developed_25_portfolios_me_inv_daily', 'developed_25_portfolios_me_op', 'developed_25_portfolios_me_op_daily', 'developed_25_portfolios_me_prior_12_2', 'developed_25_portfolios_me_prior_250_20_daily', 'developed_32_portfolios_me_be-me_inv_2x4x4', 'developed_32_portfolios_me_be-me_op_2x4x4', 'developed_32_portfolios_me_inv_op_2x4x4', 'developed_6_portfolios_me_be-me', 'developed_6_portfolios_me_be-me_daily', 'developed_6_portfolios_me_inv', 'developed_6_portfolios_me_inv_daily', 'developed_6_portfolios_me_op', 'developed_6_portfolios_me_op_daily', 'developed_6_portfolios_me_prior_12_2', 'developed_6_portfolios_me_prior_250_20_daily', 'developed_ex_us_25_portfolios_me_be-me', 'developed_ex_us_25_portfolios_me_be-me_daily', 'developed_ex_us_25_portfolios_me_inv', 'developed_ex_us_25_portfolios_me_inv_daily', 'developed_ex_us_25_portfolios_me_op', 'developed_ex_us_25_portfolios_me_op_daily', 'developed_ex_us_25_portfolios_me_prior_12_2', 'developed_ex_us_25_portfolios_me_prior_250_20_daily', 'developed_ex_us_32_portfolios_me_be-me_inv_2x4x4', 'developed_ex_us_32_portfolios_me_be-me_op_2x4x4', 'developed_ex_us_32_portfolios_me_inv_op_2x4x4', 'developed_ex_us_6_portfolios_me_be-me', 'developed_ex_us_6_portfolios_me_be-me_daily', 'developed_ex_us_6_portfolios_me_inv', 'developed_ex_us_6_portfolios_me_inv_daily', 'developed_ex_us_6_portfolios_me_op', 'developed_ex_us_6_portfolios_me_op_daily', 'developed_ex_us_6_portfolios_me_prior_12_2', 'developed_ex_us_6_portfolios_me_prior_250_20_daily', 'emerging_markets_4_portfolios_be-me_inv', 'emerging_markets_4_portfolios_be-me_op', 'emerging_markets_4_portfolios_op_inv', 'emerging_markets_6_portfolios_me_be-me', 'emerging_markets_6_portfolios_me_inv', 'emerging_markets_6_portfolios_me_op', 'emerging_markets_6_portfolios_me_prior_12_2', 'europe_25_portfolios_me_be-me', 'europe_25_portfolios_me_be-me_daily', 'europe_25_portfolios_me_inv', 'europe_25_portfolios_me_inv_daily', 'europe_25_portfolios_me_op', 'europe_25_portfolios_me_op_daily', 'europe_25_portfolios_me_prior_12_2', 'europe_25_portfolios_me_prior_250_20_daily', 'europe_32_portfolios_me_be-me_inv_2x4x4', 'europe_32_portfolios_me_be-me_op_2x4x4', 'europe_32_portfolios_me_inv_op_2x4x4', 'europe_6_portfolios_me_be-me', 'europe_6_portfolios_me_be-me_daily', 'europe_6_portfolios_me_inv', 'europe_6_portfolios_me_inv_daily', 'europe_6_portfolios_me_op', 'europe_6_portfolios_me_op_daily', 'europe_6_portfolios_me_prior_12_2', 'europe_6_portfolios_me_prior_250_20_daily', 'japan_25_portfolios_me_be-me', 'japan_25_portfolios_me_be-me_daily', 'japan_25_portfolios_me_inv', 'japan_25_portfolios_me_inv_daily', 'japan_25_portfolios_me_op', 'japan_25_portfolios_me_op_daily', 'japan_25_portfolios_me_prior_12_2', 'japan_25_portfolios_me_prior_250_20_daily', 'japan_32_portfolios_me_be-me_inv_2x4x4', 'japan_32_portfolios_me_be-me_op_2x4x4', 'japan_32_portfolios_me_inv_op_2x4x4', 'japan_6_portfolios_me_be-me', 'japan_6_portfolios_me_be-me_daily', 'japan_6_portfolios_me_inv', 'japan_6_portfolios_me_inv_daily', 'japan_6_portfolios_me_op', 'japan_6_portfolios_me_op_daily', 'japan_6_portfolios_me_prior_12_2', 'japan_6_portfolios_me_prior_250_20_daily', 'north_america_25_portfolios_me_be-me', 'north_america_25_portfolios_me_be-me_daily', 'north_america_25_portfolios_me_inv', 'north_america_25_portfolios_me_inv_daily', 'north_america_25_portfolios_me_op', 'north_america_25_portfolios_me_op_daily', 'north_america_25_portfolios_me_prior_12_2', 'north_america_25_portfolios_me_prior_250_20_daily', 'north_america_32_portfolios_me_be-me_inv_2x4x4', 'north_america_32_portfolios_me_be-me_op_2x4x4', 'north_america_32_portfolios_me_inv_op_2x4x4', 'north_america_6_portfolios_me_be-me', 'north_america_6_portfolios_me_be-me_daily', 'north_america_6_portfolios_me_inv', 'north_america_6_portfolios_me_inv_daily', 'north_america_6_portfolios_me_op', 'north_america_6_portfolios_me_op_daily', 'north_america_6_portfolios_me_prior_12_2', 'north_america_6_portfolios_me_prior_250_20_daily'] | None]`: The specific portfolio file to fetch.
  - `--measure` (Opcional) `[Literal['value', 'equal', 'number_of_firms', 'firm_size'] | None]`: The measure to fetch for the portfolio.
  - `--frequency` (Opcional) `[Literal['monthly', 'annual'] | None]`: The frequency of the data to fetch. Ignored when the portfolio ends with 'daily'.
  - `--start_date` (Opcional) `[date | None | str]`: The start date for the data. Defaults to the earliest available date.
  - `--end_date` (Opcional) `[date | None | str]`: The end date for the data. Defaults to the latest available date.

---
### Comando: `/famafrench/country_portfolio_returns`

**Descripción:** Country portfolio returns.

Metadata for the selected dataset are returned in the
`extra['results_metadata']` field of the response.

Source
------

https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html

We form value and growth portfolios in each country using four valuation ratios:

- book-to-market (B/M)
- earnings-price (E/P)
- cash earnings to price (CE/P)
- dividend yield (D/P)

We form the portfolios at the end of December each year by sorting on one of the four ratios and
then compute value-weighted returns for the following 12 months.

The value portfolios (High) contain firms in the top 30% of a ratio
and the growth portfolios (Low) contain firms in the bottom 30%.

There are two sets of portfolios.

In one, firms are included only if we have data on all four ratios.

In the other, a firm is included in a sort variable's portfolios
if we have data for that variable.

The market return (Mkt) for the first set is the value weighted average of the returns
for only firms with all four ratios.

The market return for the second set includes all firms with book-to-market data,
and Firms is the number of firms with B/M data.

- **Proveedores disponibles / soportados:** `famafrench`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `famafrench`:*
  - `--country` (Opcional) `[Literal['austria', 'australia', 'belgium', 'canada', 'denmark', 'finland', 'france', 'germany', 'hong_kong', 'ireland', 'italy', 'japan', 'malaysia', 'netherlands', 'new_zealand', 'norway', 'singapore', 'spain', 'sweden', 'switzerland', 'united_kingdom'] | None]`: Country to fetch the portfolio returns for.
  - `--measure` (Opcional) `[Literal['usd', 'local', 'ratios'] | None]`: The measure to fetch for the portfolio. Only 'annual' frequency is supported for 'ratios'.
  - `--frequency` (Opcional) `[Literal['monthly', 'annual'] | None]`: The frequency of the data to fetch. Ignored when `measure` is set to 'ratios'.
  - `--dividends` (Opcional) `[bool | None]`: When False, portoflios exclude dividends.
  - `--all_data_items_required` (Opcional) `[bool | None]`: If True (default), includes firms with data for all four ratios. When False, includes only firms with Book-to-Market (B/M) data.
  - `--start_date` (Opcional) `[date | None | str]`: The start date for the data. Defaults to the earliest available date.
  - `--end_date` (Opcional) `[date | None | str]`: The end date for the data. Defaults to the latest available date.

---
### Comando: `/famafrench/international_index_returns`

**Descripción:** International index returns.

Metadata for the selected dataset are returned in the
`extra['results_metadata']` field of the response.

See the `country_portfolio_returns` endpoint for more details.

Source
------

https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html

The returns on the index portfolios are constructed by
averaging the returns on the country portfolios.

We weight countries in the index portfolios in proportion to their EAFE + Canada weights.

Each country is added to the index portfolios when the return data for the country begin;
the country start dates can be inferred from the country return files.

- **Proveedores disponibles / soportados:** `famafrench`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `famafrench`:*
  - `--index` (Opcional) `[Literal['uk', 'scandinavia', 'europe', 'europe_ex_uk', 'asia_pacific', 'all'] | None]`: International index to fetch the portfolio returns for. Defaults to 'all'.
  - `--measure` (Opcional) `[Literal['usd', 'local', 'ratios'] | None]`: The measure to fetch for the portfolio. Only 'annual' frequency is supported for 'ratios'.
  - `--frequency` (Opcional) `[Literal['monthly', 'annual'] | None]`: The frequency of the data to fetch. Ignored when `measure` is set to 'ratios'.
  - `--dividends` (Opcional) `[bool | None]`: When False, portoflios exclude dividends.
  - `--all_data_items_required` (Opcional) `[bool | None]`: If True (default), includes firms with data for all four ratios. When False, includes only firms with Book-to-Market (B/M) data.
  - `--start_date` (Opcional) `[date | None | str]`: The start date for the data. Defaults to the earliest available date.
  - `--end_date` (Opcional) `[date | None | str]`: The end date for the data. Defaults to the latest available date.

---
### Comando: `/famafrench/breakpoints`

**Descripción:** Fama-French breakpoints.

Metadata for the selected dataset are returned in the
`extra['results_metadata']` field of the response.

Source
------

https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html#Breakpoints

- **Proveedores disponibles / soportados:** `famafrench`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `famafrench`:*
  - `--breakpoint_type` (Opcional) `[Literal['me', 'be-me', 'op', 'inv', 'e-p', 'cf-p', 'd-p', '2-12'] | None]`: Type of breakpoint to fetch.  The breakpoints for month t use all NYSE stocks that have a CRSP share code of 10 or 11 and have good shares and price data. We exclude closed end funds and REITs.  Breakpoints are computed either monthly or annually, see the description of each breakpoint type below.  Data contains every fifth percentile, from 5% to 100%.  ME --  Market Equity. Market equity (size) is price times shares outstanding. Price and shares outstanding are from CRSP.  ME breakpoints are computed for each month. It is price times shares outstanding (divided by 1,000,000) at month end.  BE/ME -----  BE/ME breakpoints are computed at the end of each June. The BE used in June of year t is the book equity for the last fiscal year end in t-1. ME is price times shares outstanding at the end of December of t-1.  The breakpoints for year t use all NYSE stocks for which we have ME for December of t-1 and (positive) BE for the last fiscal year end in t-1.  Operating Profitability -----------------------  Operating Profitability breakpoints are computed at the end of each June. OP for June of year t is annual revenues minus  - cost of goods sold - interest expense - selling, general, and administrative expenses  divided by book equity for the last fiscal year end in t-1.  Please be aware that some of the value-weight averages of operating profitability for deciles 1 and 10 are extreme. These are driven by extraordinary values of OP for individual firms. We have spot checked the accounting data that produce the extraordinary values and all the numbers we examined accurately reflect the data in the firm's accounting statements.  The breakpoints for year t use all NYSE stocks for which we have (positive) book equity data for t-1, non-missing revenues data for t-1, and non-missing data for at least one of the following:  - cost of goods sold - selling, general and administrative expenses - interest expense for t-1.  Investment ----------  Investment breakpoints are computed at the end of each June. Inv used in June of year t is the change in total assets from the fiscal year ending in year t-2 to the fiscal year ending in t-1, divided by t-2 total assets.  The breakpoints for year t use all NYSE stocks for which we have total assets data for t-2 and t-1.  E/P ---  E/P (in percent) breakpoints are computed at the end of each June. The E used in June of year t is the earnings for the last fiscal year end in t-1. P (actually ME) is price times shares outstanding at the end of December of t-1.  The breakpoints for year t use all NYSE stocks for which we have ME for December of t-1 and (positive) earnings for the last fiscal year end in t-1.  CF/P ----  CF/P (in percent) breakpoints is computed at the end of each June. The CF used in June of year t is the cash flow for the last fiscal year end in t-1. P (actually ME) is price times shares outstanding at the end of December of t-1.  The breakpoints for year t use all NYSE stocks for which we have ME for December of t-1 and (positive) cash flow for the last fiscal year end in t-1.  D/P ---  D/P (in percent) breakpoints are computed at the end of each June. The dividend yield in June of year t is the total dividends paid from July of t-1 to June of t per dollar of equity in June of t.  The breakpoints for year t use NYSE stocks for which we have at least seven months (to compute the dividend yield) from July of t-1 to June of t. (Only six monthly returns are required in June 1926.) We do not include stocks that pay no dividends from July of t-1 to June of t.  Prior 2-12 ----------  Prior return breakpoints are computed for each month. The prior return at the end of month t is the cumulative return from month t-11 to month t-1.  The breakpoints for month t use NYSE stocks. To be included, a stock must have a price for the end of month t-12 and a good return for t-1. In addition, any missing returns from t-11 to t-2 must be -99.0, CRSP's code for a missing price.
  - `--start_date` (Opcional) `[date | None | str]`: Start date for the data.
  - `--end_date` (Opcional) `[date | None | str]`: End date for the data.

---
### Comando: `/fixedincome/rate/ameribor`

**Descripción:** AMERIBOR.

AMERIBOR (short for the American interbank offered rate) is a benchmark interest rate that reflects the true cost of
short-term interbank borrowing. This rate is based on transactions in overnight unsecured loans conducted on the
American Financial Exchange (AFX).

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--maturity` (Opcional) `[Literal['all', 'overnight', 'average_30d', 'average_90d', 'term_30d', 'term_90d'] | None]`: Period of AMERIBOR rate.
  - `--frequency` (Opcional) `[Literal['a', 'q', 'm', 'w', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'] | None]`: Frequency aggregation to convert daily data to lower frequency.     a = Annual     q = Quarterly     m = Monthly     w = Weekly     wef = Weekly, Ending Friday     weth = Weekly, Ending Thursday     wew = Weekly, Ending Wednesday     wetu = Weekly, Ending Tuesday     wem = Weekly, Ending Monday     wesu = Weekly, Ending Sunday     wesa = Weekly, Ending Saturday     bwew = Biweekly, Ending Wednesday     bwem = Biweekly, Ending Monday
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type     None = No transformation     chg = Change     ch1 = Change from Year Ago     pch = Percent Change     pc1 = Percent Change from Year Ago     pca = Compounded Annual Rate of Change     cch = Continuously Compounded Rate of Change     cca = Continuously Compounded Annual Rate of Change     log = Natural Log

---
### Comando: `/fixedincome/rate/sonia`

**Descripción:** Sterling Overnight Index Average.

SONIA (Sterling Overnight Index Average) is an important interest rate benchmark. SONIA is based on actual
transactions and reflects the average of the interest rates that banks pay to borrow sterling overnight from other
financial institutions and other institutional investors.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--parameter` (Opcional) `[Literal['rate', 'index', '10th_percentile', '25th_percentile', '75th_percentile', '90th_percentile', 'total_nominal_value'] | None]`: Period of SONIA rate.

---
### Comando: `/fixedincome/rate/sofr`

**Descripción:** Secured Overnight Financing Rate.

The Secured Overnight Financing Rate (SOFR) is a broad measure of the cost of
borrowing cash overnight collateralizing by Treasury securities.

- **Proveedores disponibles / soportados:** `federal_reserve, fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `federal_reserve`:*

  *Exclusivos del proveedor `fred`:*
  - `--frequency` (Opcional) `[Literal['a', 'q', 'm', 'w', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'] | None]`: Frequency aggregation to convert daily data to lower frequency.             a = Annual             q = Quarterly             m = Monthly             w = Weekly             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log

---
### Comando: `/fixedincome/rate/iorb`

**Descripción:** Interest on Reserve Balances.

Get Interest Rate on Reserve Balances data A bank rate is the interest rate a nation's central bank charges to its
domestic banks to borrow money. The rates central banks charge are set to stabilize the economy. In the
United States, the Federal Reserve System's Board of Governors set the bank rate, also known as the discount rate.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*

---
### Comando: `/fixedincome/rate/effr`

**Descripción:** Fed Funds Rate.

Get Effective Federal Funds Rate data. A bank rate is the interest rate a nation's central bank charges to its
domestic banks to borrow money. The rates central banks charge are set to stabilize the economy.

- **Proveedores disponibles / soportados:** `federal_reserve, fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `federal_reserve`:*

  *Exclusivos del proveedor `fred`:*
  - `--frequency` (Opcional) `[Literal['a', 'q', 'm', 'w', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'] | None]`: Frequency aggregation to convert daily data to lower frequency.             a = Annual             q = Quarterly             m = Monthly             w = Weekly             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log
  - `--effr_only` (Opcional) `[bool | None]`: Return data without quantiles, target ranges, and volume.

---
### Comando: `/fixedincome/rate/effr_forecast`

**Descripción:** Fed Funds Rate Projections.

The projections for the federal funds rate are the value of the midpoint of the
projected appropriate target range for the federal funds rate or the projected
appropriate target level for the federal funds rate at the end of the specified
calendar year or over the longer run.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `fred`:*
  - `--long_run` (Opcional) `[bool | None]`: Flag to show long run projections

---
### Comando: `/fixedincome/rate/estr`

**Descripción:** Euro Short-Term Rate.

The euro short-term rate (€STR) reflects the wholesale euro unsecured overnight borrowing costs of banks located in
the euro area. The €STR is published on each TARGET2 business day based on transactions conducted and settled on
the previous TARGET2 business day (the reporting date “T”) with a maturity date of T+1 which are deemed to have been
executed at arm's length and thus reflect market rates in an unbiased way.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--frequency` (Opcional) `[Literal['a', 'q', 'm', 'w', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'] | None]`: Frequency aggregation to convert daily data to lower frequency.              a = Annual              q = Quarterly              m = Monthly              w = Weekly              d = Daily              wef = Weekly, Ending Friday              weth = Weekly, Ending Thursday              wew = Weekly, Ending Wednesday              wetu = Weekly, Ending Tuesday              wem = Weekly, Ending Monday              wesu = Weekly, Ending Sunday              wesa = Weekly, Ending Saturday              bwew = Biweekly, Ending Wednesday              bwem = Biweekly, Ending Monday
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.              avg = Average              sum = Sum              eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type              None = No transformation              chg = Change              ch1 = Change from Year Ago              pch = Percent Change              pc1 = Percent Change from Year Ago              pca = Compounded Annual Rate of Change              cch = Continuously Compounded Rate of Change              cca = Continuously Compounded Annual Rate of Change              log = Natural Log

---
### Comando: `/fixedincome/rate/ecb`

**Descripción:** European Central Bank Interest Rates.

The Governing Council of the ECB sets the key interest rates for the euro area:

- The interest rate on the main refinancing operations (MRO), which provide
the bulk of liquidity to the banking system.
- The rate on the deposit facility, which banks may use to make overnight deposits with the Eurosystem.
- The rate on the marginal lending facility, which offers overnight credit to banks from the Eurosystem.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--interest_rate_type` (Opcional) `[Literal['deposit', 'lending', 'refinancing'] | None]`: The type of interest rate.

  *Exclusivos del proveedor `fred`:*

---
### Comando: `/fixedincome/rate/dpcredit`

**Descripción:** Discount Window Primary Credit Rate.

A bank rate is the interest rate a nation's central bank charges to its domestic banks to borrow money.
The rates central banks charge are set to stabilize the economy.
In the United States, the Federal Reserve System's Board of Governors set the bank rate,
also known as the discount rate.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--parameter` (Opcional) `[Literal['daily_excl_weekend', 'monthly', 'weekly', 'daily', 'annual'] | None]`: FRED series ID of DWPCR data.

---
### Comando: `/fixedincome/rate/overnight_bank_funding`

**Descripción:** Overnight Bank Funding.

For the United States, the overnight bank funding rate (OBFR) is calculated as a volume-weighted median of
overnight federal funds transactions and Eurodollar transactions reported in the
FR 2420 Report of Selected Money Market Rates.

- **Proveedores disponibles / soportados:** `federal_reserve, fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `federal_reserve`:*

  *Exclusivos del proveedor `fred`:*
  - `--frequency` (Opcional) `[Literal['a', 'q', 'm', 'w', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'] | None]`: Frequency aggregation to convert daily data to lower frequency.             a = Annual             q = Quarterly             m = Monthly             w = Weekly             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log

---
### Comando: `/fixedincome/spreads/tcm`

**Descripción:** Treasury Constant Maturity.

Get data for 10-Year Treasury Constant Maturity Minus Selected Treasury Constant Maturity.
Constant maturity is the theoretical value of a U.S. Treasury that is based on recent values of auctioned U.S.
Treasuries. The value is obtained by the U.S. Treasury on a daily basis through interpolation of the Treasury
yield curve which, in turn, is based on closing bid-yields of actively-traded Treasury securities.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--maturity` (Opcional) `[Literal['3m', '2y'] | None]`: The maturity

  *Exclusivos del proveedor `fred`:*

---
### Comando: `/fixedincome/spreads/tcm_effr`

**Descripción:** Select Treasury Constant Maturity.

Get data for Selected Treasury Constant Maturity Minus Federal Funds Rate
Constant maturity is the theoretical value of a U.S. Treasury that is based on recent values of auctioned U.S.
Treasuries. The value is obtained by the U.S. Treasury on a daily basis through interpolation of the Treasury
yield curve which, in turn, is based on closing bid-yields of actively-traded Treasury securities.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--maturity` (Opcional) `[Literal['10y', '5y', '1y', '6m', '3m'] | None]`: The maturity

  *Exclusivos del proveedor `fred`:*

---
### Comando: `/fixedincome/spreads/treasury_effr`

**Descripción:** Select Treasury Bill.

Get Selected Treasury Bill Minus Federal Funds Rate.
Constant maturity is the theoretical value of a U.S. Treasury that is based on recent values of
auctioned U.S. Treasuries.
The value is obtained by the U.S. Treasury on a daily basis through interpolation of the Treasury
yield curve which, in turn, is based on closing bid-yields of actively-traded Treasury securities.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--maturity` (Opcional) `[Literal['3m', '6m'] | None]`: The maturity

  *Exclusivos del proveedor `fred`:*

---
### Comando: `/fixedincome/government/yield_curve`

**Descripción:** Get yield curve data by country and date.

- **Proveedores disponibles / soportados:** `ecb, econdb, federal_reserve, fmp, fred`

**Flags / Parámetros (Standard & Providers):**
  - `--date` (Opcional) `[date | str | None | list[date | str | None]]`: A specific date to get data for. By default is the current data. Multiple items allowed for provider(s): ecb, econdb, federal_reserve, fmp, fred.

  *Exclusivos del proveedor `ecb`:*
  - `--rating` (Opcional) `[Literal['aaa', 'all_ratings'] | None]`: The rating type, either 'aaa' or 'all_ratings'.
  - `--yield_curve_type` (Opcional) `[Literal['spot_rate', 'instantaneous_forward', 'par_yield'] | None]`: The yield curve type.
  - `--use_cache` (Opcional) `[bool | None]`: If true, cache the request for four hours.

  *Exclusivos del proveedor `econdb`:*
  - `--country` (Opcional) `[str | None]`: The country to get data. New Zealand, Mexico, Singapore, and Thailand have only monthly data. The nearest date to the requested one will be used.
  - `--use_cache` (Opcional) `[bool | None]`: If true, cache the request for four hours.

  *Exclusivos del proveedor `federal_reserve`:*

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `fred`:*
  - `--yield_curve_type` (Opcional) `[Literal['nominal', 'real', 'breakeven', 'treasury_minus_fed_funds', 'corporate_spot', 'corporate_par'] | None]`: Yield curve type. Nominal and Real Rates are available daily, others are monthly. The closest date to the requested date will be returned.

---
### Comando: `/fixedincome/government/treasury_rates`

**Descripción:** Government Treasury Rates.

- **Proveedores disponibles / soportados:** `federal_reserve, fmp`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `federal_reserve`:*

  *Exclusivos del proveedor `fmp`:*

---
### Comando: `/fixedincome/government/treasury_auctions`

**Descripción:** Government Treasury Auctions.

- **Proveedores disponibles / soportados:** `government_us`

**Flags / Parámetros (Standard & Providers):**
  - `--security_type` (Opcional) `[Literal['bill', 'note', 'bond', 'cmb', 'tips', 'frn'] | None]`: Used to only return securities of a particular type.
  - `--cusip` (Opcional) `[str | None]`: Filter securities by CUSIP.
  - `--page_size` (Opcional) `[int | None]`: Maximum number of results to return; you must also include pagenum when using pagesize.
  - `--page_num` (Opcional) `[int | None]`: The first page number to display results for; used in combination with page size.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format. The default is 90 days ago.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format. The default is today.

  *Exclusivos del proveedor `government_us`:*

---
### Comando: `/fixedincome/government/treasury_prices`

**Descripción:** Government Treasury Prices by date.

- **Proveedores disponibles / soportados:** `government_us, tmx`

**Flags / Parámetros (Standard & Providers):**
  - `--date` (Opcional) `[date | None | str]`: A specific date to get data for. Defaults to the last business day.

  *Exclusivos del proveedor `government_us`:*
  - `--cusip` (Opcional) `[str | None]`: Filter by CUSIP.
  - `--security_type` (Opcional) `[Literal['bill', 'note', 'bond', 'tips', 'frn'] | None]`: Filter by security type.

  *Exclusivos del proveedor `tmx`:*
  - `--govt_type` (Opcional) `[Literal['federal', 'provincial', 'municipal'] | None]`: The level of government issuer.
  - `--issue_date_min` (Opcional) `[date | None]`: Filter by the minimum original issue date.
  - `--issue_date_max` (Opcional) `[date | None]`: Filter by the maximum original issue date.
  - `--last_traded_min` (Opcional) `[date | None]`: Filter by the minimum last trade date.
  - `--maturity_date_min` (Opcional) `[date | None]`: Filter by the minimum maturity date.
  - `--maturity_date_max` (Opcional) `[date | None]`: Filter by the maximum maturity date.
  - `--use_cache` (Opcional) `[bool | None]`: All bond data is sourced from a single JSON file that is updated daily. The file is cached for one day to eliminate downloading more than once. Caching will significantly speed up subsequent queries. To bypass, set to False.

---
### Comando: `/fixedincome/government/tips_yields`

**Descripción:** Get current Treasury inflation-protected securities yields.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--maturity` (Opcional) `[Literal['5', '10', '20', '30'] | None]`: The maturity of the security in years - 5, 10, 20, 30 - defaults to all. Note that the maturity is the tenor of the security, not the time to maturity.
  - `--frequency` (Opcional) `[Literal['a', 'q', 'm', 'w', 'd', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'] | None]`: Frequency aggregation to convert high frequency data to lower frequency.             None = No change             a = Annual             q = Quarterly             m = Monthly             w = Weekly             d = Daily             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca'] | None]`: Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change

---
### Comando: `/fixedincome/corporate/hqm`

**Descripción:** High Quality Market Corporate Bond.

The HQM yield curve represents the high quality corporate bond market, i.e.,
corporate bonds rated AAA, AA, or A.  The HQM curve contains two regression terms.
These terms are adjustment factors that blend AAA, AA, and A bonds into a single HQM yield curve
that is the market-weighted average (MWA) quality of high quality bonds.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--date` (Opcional) `[date | str | None | list[date | str | None]]`: A specific date to get data for. Multiple items allowed for provider(s): fred.

  *Exclusivos del proveedor `fred`:*
  - `--yield_curve` (Opcional) `[Literal['spot', 'par'] | None]`: The yield curve type.

---
### Comando: `/fixedincome/corporate/spot_rates`

**Descripción:** Spot Rates.

The spot rates for any maturity is the yield on a bond that provides a single payment at that maturity.
This is a zero coupon bond.
Because each spot rate pertains to a single cashflow, it is the relevant interest rate
concept for discounting a pension liability at the same maturity.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--maturity` (Opcional) `[float | str | None | list[float | str | None]]`: Maturities in years. Multiple items allowed for provider(s): fred.
  - `--category` (Opcional) `[str | None | list[str | None]]`: Rate category. Options: spot_rate, par_yield. Multiple items allowed for provider(s): fred.

  *Exclusivos del proveedor `fred`:*

---
### Comando: `/fixedincome/corporate/commercial_paper`

**Descripción:** Commercial Paper.

Commercial paper (CP) consists of short-term, promissory notes issued primarily by corporations.
Maturities range up to 270 days but average about 30 days.
Many companies use CP to raise cash needed for current transactions,
and many find it to be a lower-cost alternative to bank loans.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--maturity` (Opcional) `[str | None]`: A target maturity.
  - `--category` (Opcional) `[str | None]`: The category of asset.
  - `--frequency` (Opcional) `[Literal['a', 'q', 'm', 'w', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'] | None]`: Frequency aggregation to convert daily data to lower frequency.             a = Annual             q = Quarterly             m = Monthly             w = Weekly             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log

---
### Comando: `/fixedincome/corporate/bond_prices`

**Descripción:** Corporate Bond Prices.

- **Proveedores disponibles / soportados:** `tmx`

**Flags / Parámetros (Standard & Providers):**
  - `--country` (Opcional) `[str | None]`: The country to get data. Matches partial name.
  - `--issuer_name` (Opcional) `[str | None]`: Name of the issuer.  Returns partial matches and is case insensitive.
  - `--isin` (Opcional) `[list | str | None | list[list | str | None]]`: International Securities Identification Number(s) of the bond(s). Multiple items allowed for provider(s): tmx.
  - `--lei` (Opcional) `[str | None]`: Legal Entity Identifier of the issuing entity.
  - `--currency` (Opcional) `[list | str | None]`: Currency of the bond. Formatted as the 3-letter ISO 4217 code (e.g. GBP, EUR, USD).
  - `--coupon_min` (Opcional) `[float | None]`: Minimum coupon rate of the bond.
  - `--coupon_max` (Opcional) `[float | None]`: Maximum coupon rate of the bond.
  - `--issued_amount_min` (Opcional) `[int | None]`: Minimum issued amount of the bond.
  - `--issued_amount_max` (Opcional) `[str | None]`: Maximum issued amount of the bond.
  - `--maturity_date_min` (Opcional) `[date | None]`: Minimum maturity date of the bond.
  - `--maturity_date_max` (Opcional) `[date | None]`: Maximum maturity date of the bond.

  *Exclusivos del proveedor `tmx`:*
  - `--issue_date_min` (Opcional) `[date | None]`: Filter by the minimum original issue date.
  - `--issue_date_max` (Opcional) `[date | None]`: Filter by the maximum original issue date.
  - `--last_traded_min` (Opcional) `[date | None]`: Filter by the minimum last trade date.
  - `--use_cache` (Opcional) `[bool | None]`: All bond data is sourced from a single JSON file that is updated daily. The file is cached for one day to eliminate downloading more than once. Caching will significantly speed up subsequent queries. To bypass, set to False.

---
### Comando: `/fixedincome/bond_indices`

**Descripción:** Bond Indices.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--index_type` (Opcional) `[Literal['yield', 'yield_to_worst', 'total_return', 'oas'] | None]`: The type of series. OAS is the option-adjusted spread. Default is yield.

  *Exclusivos del proveedor `fred`:*
  - `--category` (Opcional) `[Literal['high_yield', 'us', 'emerging_markets'] | None]`: The type of index category. Used in conjunction with 'index', default is 'us'.
  - `--index` (Opcional) `[str | None]`: The specific index to query. Used in conjunction with 'category' and 'index_type', default is 'yield_curve'.         Possible values are:             corporate             seasoned_corporate             liquid_corporate             yield_curve             crossover             public_sector             private_sector             non_financial             high_grade             high_yield             liquid_emea             emea             liquid_asia             asia             liquid_latam             latam             liquid_aaa             liquid_bbb             aaa             aa             a             bbb             bb             b             ccc
  - `--frequency` (Opcional) `[Literal['a', 'q', 'm', 'w', 'd', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'] | None]`: Frequency aggregation to convert daily data to lower frequency.             None = No change             a = Annual             q = Quarterly             m = Monthly             w = Weekly             d = Daily             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set, default is 'avg'.             avg = Average             sum = Sum             eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log

---
### Comando: `/fixedincome/mortgage_indices`

**Descripción:** Mortgage Indices.

- **Proveedores disponibles / soportados:** `fred`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `fred`:*
  - `--index` (Opcional) `[Literal['primary', 'ltv_lte_80', 'ltv_gt_80', 'conforming_30y', 'conforming_30y_na', 'jumbo_30y', 'fha_30y', 'va_30y', 'usda_30y', 'conforming_15y', 'ltv_lte80_fico_ge740', 'ltv_lte80_fico_a720b739', 'ltv_lte80_fico_a700b719', 'ltv_lte80_fico_a680b699', 'ltv_lte80_fico_lt680', 'ltv_gt80_fico_ge740', 'ltv_gt80_fico_a720b739', 'ltv_gt80_fico_a700b719', 'ltv_gt80_fico_a680b699', 'ltv_gt80_fico_lt680'] | None]`: The specific index, or index group, to query. Default is the 'primary' group.
  - `--frequency` (Opcional) `[Literal['a', 'q', 'm', 'w', 'd', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'] | None]`: Frequency aggregation to convert daily data to lower frequency.             None = No change             a = Annual             q = Quarterly             m = Monthly             w = Weekly             d = Daily             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday
  - `--aggregation_method` (Opcional) `[Literal['avg', 'sum', 'eop'] | None]`: A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set, default is 'avg'.             avg = Average             sum = Sum             eop = End of Period
  - `--transform` (Opcional) `[Literal['chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'] | None]`: Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log

---
### Comando: `/imf_utils/list_dataflows`

**Descripción:** list all available IMF dataflows.

Returns an OBBject containing either a JSON dictionary of dataflows
or a markdown string under the 'results' attribute.

**Flags / Parámetros (Standard & Providers):**
  - `--output_format` (Opcional) `[Literal['json', 'markdown']]`: 

---
### Comando: `/imf_utils/get_dataflow_dimensions`

**Descripción:** Dataflow parameters and possible values.

Returns an OBBject containing either a JSON dictionary of parameters
and their options, or a markdown string under the 'results' attribute.

**Flags / Parámetros (Standard & Providers):**
  - `--dataflow_id` *(Requerido)* `[str]`: 
  - `--output_format` (Opcional) `[Literal['json', 'markdown']]`: 

---
### Comando: `/imf_utils/list_port_id_choices`

**Descripción:** Get port ID choices for IMF Port Watch.

Returns
-------
list[dict[str, str]]
 A list of dictionaries with 'label' and 'value' for each port ID.

**Flags / Parámetros (Standard & Providers):**

---
### Comando: `/imf_utils/list_tables`

**Descripción:** Get the list of presentation tables available from the IMF.

**Flags / Parámetros (Standard & Providers):**

---
### Comando: `/imf_utils/list_table_choices`

**Descripción:** Get presentation table choices for IMF data retrieval.

Returns
-------
list[dict[str, str]]
 A list of dictionaries with 'label' and 'value' for each presentation table.

**Flags / Parámetros (Standard & Providers):**

---
### Comando: `/imf_utils/list_dataflow_choices`

**Descripción:** Get dataflow choices for IMF data retrieval.

Returns
-------
list[dict[str, str]]
 A list of dictionaries with 'label' and 'value' for each presentation table.

**Flags / Parámetros (Standard & Providers):**

---
### Comando: `/imf_utils/presentation_table_choices`

**Descripción:** Get presentation table choices for IMF data retrieval.

This endpoint provides dynamic choices for IMF presentation tables based on selected parameters.
It is intended to be used by the OpenBB Workspace UI to populate dropdowns.

For manual API calls, use `economy/indicators` instead with a `symbol` from `list_tables()`.

**Flags / Parámetros (Standard & Providers):**
  - `--dataflow_group` (Opcional) `[str | None]`: 
  - `--table` (Opcional) `[str | None]`: 
  - `--country` (Opcional) `[str | None]`: 
  - `--frequency` (Opcional) `[str | None]`: 

---
### Comando: `/imf_utils/presentation_table`

**Descripción:** Get a formatted presentation table from the IMF database. Returns as HTML or JSON list.

**Flags / Parámetros (Standard & Providers):**
  - `--dataflow_group` (Opcional) `[str | None]`: 
  - `--table` (Opcional) `[str | None]`: 
  - `--country` (Opcional) `[str | None]`: 
  - `--frequency` (Opcional) `[str | None]`: 
  - `--dimension_values` (Opcional) `[list[str] | str | None]`: 
  - `--limit` (Opcional) `[int]`: 
  - `--raw` (Opcional) `[bool]`: 

---
### Comando: `/index/price/historical`

**Descripción:** Historical Index Levels.

- **Proveedores disponibles / soportados:** `cboe, fmp, intrinio, polygon, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str | list[str]]`: Symbol to get data for. Multiple items allowed for provider(s): cboe, fmp, intrinio, polygon, yfinance.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `cboe`:*
  - `--interval` (Opcional) `[Literal['1m', '1d'] | None]`: Time interval of the data to return. The most recent trading day is not including in daily historical data. Intraday data is only available for the most recent trading day at 1 minute intervals.
  - `--use_cache` (Opcional) `[bool | None]`: When True, the company directories will be cached for 24 hours and are used to validate symbols. The results of the function are not cached. Set as False to bypass.

  *Exclusivos del proveedor `fmp`:*
  - `--interval` (Opcional) `[Literal['1m', '5m', '1h', '1d'] | None]`: Time interval of the data to return.

  *Exclusivos del proveedor `intrinio`:*
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `polygon`:*
  - `--interval` (Opcional) `[str | None]`: Time interval of the data to return. The numeric portion of the interval can be any positive integer. The letter portion can be one of the following: s, m, h, d, W, M, Q, Y
  - `--sort` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order of the data. This impacts the results in combination with the 'limit' parameter. The results are always returned in ascending order by date.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `yfinance`:*
  - `--interval` (Opcional) `[Literal['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1W', '1M', '1Q'] | None]`: Time interval of the data to return.

---
### Comando: `/index/constituents`

**Descripción:** Get Index Constituents.

- **Proveedores disponibles / soportados:** `cboe, fmp, tmx`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `cboe`:*
  - `--symbol` (Opcional) `[Literal['BAT20P', 'BBE20P', 'BCH20P', 'BCHM30P', 'BDE40P', 'BDEM50P', 'BDES50P', 'BDK25P', 'BEP50P', 'BEPACP', 'BEPBUS', 'BEPCNC', 'BEPCONC', 'BEPCONS', 'BEPENGY', 'BEPFIN', 'BEPHLTH', 'BEPIND', 'BEPNEM', 'BEPTEC', 'BEPTEL', 'BEPUTL', 'BEPXUKP', 'BES35P', 'BEZ50P', 'BEZACP', 'BFI25P', 'BFR40P', 'BFRM20P', 'BIE20P', 'BIT40P', 'BNL25P', 'BNLM25P', 'BNO25G', 'BNORD40P', 'BPT20P', 'BSE30P', 'BUK100P', 'BUK250P', 'BUK350P', 'BUKAC', 'BUKBISP', 'BUKBUS', 'BUKCNC', 'BUKCONC', 'BUKCONS', 'BUKENGY', 'BUKFIN', 'BUKHI50P', 'BUKHLTH', 'BUKIND', 'BUKLO50P', 'BUKMINP', 'BUKNEM', 'BUKSC', 'BUKTEC', 'BUKTEL', 'BUKUTL'] | None]`: None

  *Exclusivos del proveedor `fmp`:*
  - `--symbol` (Opcional) `[Literal['dowjones', 'sp500', 'nasdaq'] | None]`: None
  - `--historical` (Opcional) `[bool | None]`: Flag to retrieve historical removals and additions.

  *Exclusivos del proveedor `tmx`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use a cached request. Index data is from a single JSON file, updated each day after close. It is cached for one day. To bypass, set to False.

---
### Comando: `/index/snapshots`

**Descripción:** Index Snapshots. Current levels for all indices from a provider, grouped by `region`.

- **Proveedores disponibles / soportados:** `cboe, tmx`

**Flags / Parámetros (Standard & Providers):**
  - `--region` (Opcional) `[str | None]`: The region of focus for the data - i.e., us, eu.

  *Exclusivos del proveedor `cboe`:*
  - `--region` (Opcional) `[Literal['us', 'eu'] | None]`: None

  *Exclusivos del proveedor `tmx`:*
  - `--region` (Opcional) `[Literal['ca', 'us'] | None]`: None
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use a cached request. Index data is from a single JSON file, updated each day after close. It is cached for one day. To bypass, set to False.

---
### Comando: `/index/available`

**Descripción:** All indices available from a given provider.

- **Proveedores disponibles / soportados:** `cboe, fmp, tmx, yfinance`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `cboe`:*
  - `--use_cache` (Opcional) `[bool | None]`: When True, the Cboe Index directory will be cached for 24 hours. Set as False to bypass.

  *Exclusivos del proveedor `fmp`:*

  *Exclusivos del proveedor `tmx`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use a cached request. Index data is from a single JSON file, updated each day after close. It is cached for one day. To bypass, set to False.

  *Exclusivos del proveedor `yfinance`:*

---
### Comando: `/index/search`

**Descripción:** Filter indices for rows containing the query.

- **Proveedores disponibles / soportados:** `cboe`

**Flags / Parámetros (Standard & Providers):**
  - `--query` (Opcional) `[str | None]`: Search query.
  - `--is_symbol` (Opcional) `[bool | None]`: Whether to search by ticker symbol.

  *Exclusivos del proveedor `cboe`:*
  - `--use_cache` (Opcional) `[bool | None]`: When True, the Cboe Index directory will be cached for 24 hours. Set as False to bypass.

---
### Comando: `/index/sp500_multiples`

**Descripción:** Get historical S&P 500 multiples and Shiller PE ratios.

- **Proveedores disponibles / soportados:** `multpl`

**Flags / Parámetros (Standard & Providers):**
  - `--series_name` (Opcional) `[Literal['shiller_pe_month', 'shiller_pe_year', 'pe_year', 'pe_month', 'dividend_year', 'dividend_month', 'dividend_growth_quarter', 'dividend_growth_year', 'dividend_yield_year', 'dividend_yield_month', 'earnings_year', 'earnings_month', 'earnings_growth_year', 'earnings_growth_quarter', 'real_earnings_growth_year', 'real_earnings_growth_quarter', 'earnings_yield_year', 'earnings_yield_month', 'real_price_year', 'real_price_month', 'inflation_adjusted_price_year', 'inflation_adjusted_price_month', 'sales_year', 'sales_quarter', 'sales_growth_year', 'sales_growth_quarter', 'real_sales_year', 'real_sales_quarter', 'real_sales_growth_year', 'real_sales_growth_quarter', 'price_to_sales_year', 'price_to_sales_quarter', 'price_to_book_value_year', 'price_to_book_value_quarter', 'book_value_year', 'book_value_quarter'] | None | list[Literal['shiller_pe_month', 'shiller_pe_year', 'pe_year', 'pe_month', 'dividend_year', 'dividend_month', 'dividend_growth_quarter', 'dividend_growth_year', 'dividend_yield_year', 'dividend_yield_month', 'earnings_year', 'earnings_month', 'earnings_growth_year', 'earnings_growth_quarter', 'real_earnings_growth_year', 'real_earnings_growth_quarter', 'earnings_yield_year', 'earnings_yield_month', 'real_price_year', 'real_price_month', 'inflation_adjusted_price_year', 'inflation_adjusted_price_month', 'sales_year', 'sales_quarter', 'sales_growth_year', 'sales_growth_quarter', 'real_sales_year', 'real_sales_quarter', 'real_sales_growth_year', 'real_sales_growth_quarter', 'price_to_sales_year', 'price_to_sales_quarter', 'price_to_book_value_year', 'price_to_book_value_quarter', 'book_value_year', 'book_value_quarter'] | None]]`: The name of the series. Defaults to 'pe_month'. Multiple items allowed for provider(s): multpl.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `multpl`:*

---
### Comando: `/index/sectors`

**Descripción:** Get Index Sectors. Sector weighting of an index.

- **Proveedores disponibles / soportados:** `tmx`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `tmx`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether to use a cached request. All Index data comes from a single JSON file that is updated daily. To bypass, set to False. If True, the data will be cached for 1 day.

---
### Comando: `/news/world`

**Descripción:** World News. Global news data.

- **Proveedores disponibles / soportados:** `benzinga, biztoc, fmp, intrinio, tiingo`

**Flags / Parámetros (Standard & Providers):**
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format. The default is 2 weeks ago.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format. The default is today.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return. The number of articles to return.

  *Exclusivos del proveedor `benzinga`:*
  - `--date` (Opcional) `[date | None | str]`: A specific date to get data for.
  - `--display` (Opcional) `[Literal['headline', 'abstract', 'full'] | None]`: Specify headline only (headline), headline + teaser (abstract), or headline + full body (full).
  - `--updated_since` (Opcional) `[int | None]`: Number of seconds since the news was updated.
  - `--published_since` (Opcional) `[int | None]`: Number of seconds since the news was published.
  - `--sort` (Opcional) `[Literal['id', 'created', 'updated'] | None]`: Key to sort the news by.
  - `--order` (Opcional) `[Literal['asc', 'desc'] | None]`: Order to sort the news by.
  - `--isin` (Opcional) `[str | None]`: The ISIN of the news to retrieve.
  - `--cusip` (Opcional) `[str | None]`: The CUSIP of the news to retrieve.
  - `--channels` (Opcional) `[str | None]`: Channels of the news to retrieve.
  - `--topics` (Opcional) `[str | None]`: Topics of the news to retrieve.
  - `--authors` (Opcional) `[str | None]`: Authors of the news to retrieve.
  - `--content_types` (Opcional) `[str | None]`: Content types of the news to retrieve.

  *Exclusivos del proveedor `biztoc`:*
  - `--term` (Opcional) `[str | None]`: Search term to filter articles by. This overrides all other filters.
  - `--source` (Opcional) `[str | None]`: Filter by a specific publisher. Only valid when filter is set to source.

  *Exclusivos del proveedor `fmp`:*
  - `--topic` (Opcional) `[Literal['fmp_articles', 'general', 'press_releases', 'stocks', 'forex', 'crypto'] | None]`: The topic of the news to be fetched.
  - `--page` (Opcional) `[int | None]`: Page number of the results. Use in combination with limit.

  *Exclusivos del proveedor `intrinio`:*
  - `--source` (Opcional) `[Literal['yahoo', 'moody', 'moody_us_news', 'moody_us_press_releases'] | None]`: The source of the news article.
  - `--sentiment` (Opcional) `[Literal['positive', 'neutral', 'negative'] | None]`: Return news only from this source.
  - `--language` (Opcional) `[str | None]`: Filter by language. Unsupported for yahoo source.
  - `--topic` (Opcional) `[str | None]`: Filter by topic. Unsupported for yahoo source.
  - `--word_count_greater_than` (Opcional) `[int | None]`: News stories will have a word count greater than this value. Unsupported for yahoo source.
  - `--word_count_less_than` (Opcional) `[int | None]`: News stories will have a word count less than this value. Unsupported for yahoo source.
  - `--is_spam` (Opcional) `[bool | None]`: Filter whether it is marked as spam or not. Unsupported for yahoo source.
  - `--business_relevance_greater_than` (Opcional) `[float | None]`: News stories will have a business relevance score more than this value. Unsupported for yahoo source. Value is a decimal between 0 and 1.
  - `--business_relevance_less_than` (Opcional) `[float | None]`: News stories will have a business relevance score less than this value. Unsupported for yahoo source. Value is a decimal between 0 and 1.

  *Exclusivos del proveedor `tiingo`:*
  - `--offset` (Opcional) `[int | None]`: Page offset, used in conjunction with limit.
  - `--source` (Opcional) `[str | None]`: A comma-separated list of the domains requested.

---
### Comando: `/news/company`

**Descripción:** Company News. Get news for one or more companies.

- **Proveedores disponibles / soportados:** `benzinga, fmp, intrinio, polygon, tiingo, tmx, yfinance`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` (Opcional) `[str | None | list[str | None]]`: Symbol to get data for. Multiple items allowed for provider(s): benzinga, fmp, intrinio, polygon, tiingo, tmx, yfinance.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return.

  *Exclusivos del proveedor `benzinga`:*
  - `--date` (Opcional) `[date | None | str]`: A specific date to get data for.
  - `--display` (Opcional) `[Literal['headline', 'abstract', 'full'] | None]`: Specify headline only (headline), headline + teaser (abstract), or headline + full body (full).
  - `--updated_since` (Opcional) `[int | None]`: Number of seconds since the news was updated.
  - `--published_since` (Opcional) `[int | None]`: Number of seconds since the news was published.
  - `--sort` (Opcional) `[Literal['id', 'created', 'updated'] | None]`: Key to sort the news by.
  - `--order` (Opcional) `[Literal['asc', 'desc'] | None]`: Order to sort the news by.
  - `--isin` (Opcional) `[str | None]`: The company's ISIN.
  - `--cusip` (Opcional) `[str | None]`: The company's CUSIP.
  - `--channels` (Opcional) `[str | None]`: Channels of the news to retrieve.
  - `--topics` (Opcional) `[str | None]`: Topics of the news to retrieve.
  - `--authors` (Opcional) `[str | None]`: Authors of the news to retrieve.
  - `--content_types` (Opcional) `[str | None]`: Content types of the news to retrieve.

  *Exclusivos del proveedor `fmp`:*
  - `--page` (Opcional) `[int | None]`: Page number of the results. Use in combination with limit.
  - `--press_release` (Opcional) `[bool | None]`: When true, will return only press releases for the given symbol(s).

  *Exclusivos del proveedor `intrinio`:*
  - `--source` (Opcional) `[Literal['yahoo', 'moody', 'moody_us_news', 'moody_us_press_releases'] | None]`: The source of the news article.
  - `--sentiment` (Opcional) `[Literal['positive', 'neutral', 'negative'] | None]`: Return news only from this source.
  - `--language` (Opcional) `[str | None]`: Filter by language. Unsupported for yahoo source.
  - `--topic` (Opcional) `[str | None]`: Filter by topic. Unsupported for yahoo source.
  - `--word_count_greater_than` (Opcional) `[int | None]`: News stories will have a word count greater than this value. Unsupported for yahoo source.
  - `--word_count_less_than` (Opcional) `[int | None]`: News stories will have a word count less than this value. Unsupported for yahoo source.
  - `--is_spam` (Opcional) `[bool | None]`: Filter whether it is marked as spam or not. Unsupported for yahoo source.
  - `--business_relevance_greater_than` (Opcional) `[float | None]`: News stories will have a business relevance score more than this value. Unsupported for yahoo source. Value is a decimal between 0 and 1.
  - `--business_relevance_less_than` (Opcional) `[float | None]`: News stories will have a business relevance score less than this value. Unsupported for yahoo source. Value is a decimal between 0 and 1.

  *Exclusivos del proveedor `polygon`:*
  - `--order` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort order of the articles.

  *Exclusivos del proveedor `tiingo`:*
  - `--offset` (Opcional) `[int | None]`: Page offset, used in conjunction with limit.
  - `--source` (Opcional) `[str | None]`: A comma-separated list of the domains requested.

  *Exclusivos del proveedor `tmx`:*
  - `--page` (Opcional) `[int | None]`: The page number to start from. Use with limit.

  *Exclusivos del proveedor `yfinance`:*

---
### Comando: `/quantitative/rolling/skew`

**Descripción:** Get Rolling Skew.

Skew is a statistical measure that reveals the degree of asymmetry of a distribution around its mean.
Positive skewness indicates a distribution with an extended tail to the right, while negative skewness shows a tail
that stretches left. Understanding skewness can provide insights into potential biases in data and help anticipate
the nature of future data points. It's particularly useful for identifying the likelihood of extreme outcomes in
financial returns, enabling more informed decision-making based on the distribution's shape over a specified period.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 
  - `--window` (Opcional) `[int]`: 
  - `--index` (Opcional) `[str]`: 

---
### Comando: `/quantitative/rolling/variance`

**Descripción:** Calculate the rolling variance of a target column within a given window size.

Variance measures the dispersion of a set of data points around their mean. It is a key metric for
assessing the volatility and stability of financial returns or other time series data over a specified rolling window.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 
  - `--window` (Opcional) `[int]`: 
  - `--index` (Opcional) `[str]`: 

---
### Comando: `/quantitative/rolling/stdev`

**Descripción:** Calculate the rolling standard deviation of a target column within a given window size.

Standard deviation is a measure of the amount of variation or dispersion of a set of values.
It is widely used to assess the risk and volatility of financial returns or other time series data
over a specified rolling window. It is the square root of the variance.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 
  - `--window` (Opcional) `[int]`: 
  - `--index` (Opcional) `[str]`: 

---
### Comando: `/quantitative/rolling/kurtosis`

**Descripción:** Calculate the rolling kurtosis of a target column within a given window size.

Kurtosis measures the "tailedness" of the probability distribution of a real-valued random variable.
High kurtosis indicates a distribution with heavy tails (outliers), suggesting a higher risk of extreme outcomes.
Low kurtosis indicates a distribution with lighter tails (less outliers), suggesting less risk of extreme outcomes.
This function helps in assessing the risk of outliers in financial returns or other time series data over a specified
rolling window.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 
  - `--window` (Opcional) `[int]`: 
  - `--index` (Opcional) `[str]`: 

---
### Comando: `/quantitative/rolling/quantile`

**Descripción:** Calculate the rolling quantile of a target column within a given window size at a specified quantile percentage.

Quantiles are points dividing the range of a probability distribution into intervals with equal probabilities,
or dividing the sample in the same way. This function is useful for understanding the distribution of data
within a specified window, allowing for analysis of trends, identification of outliers, and assessment of risk.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 
  - `--window` (Opcional) `[int]`: 
  - `--quantile_pct` (Opcional) `[float]`: 
  - `--index` (Opcional) `[str]`: 

---
### Comando: `/quantitative/rolling/mean`

**Descripción:** Calculate the rolling average of a target column within a given window size.

The rolling mean is a simple moving average that calculates the average of a target variable over a specified window.
This function is widely used in financial analysis to smooth short-term fluctuations and highlight longer-term trends
or cycles in time series data.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 
  - `--window` (Opcional) `[int]`: 
  - `--index` (Opcional) `[str]`: 

---
### Comando: `/quantitative/stats/skew`

**Descripción:** Get the skew of the data set.

Skew is a statistical measure that reveals the degree of asymmetry of a distribution around its mean.
Positive skewness indicates a distribution with an extended tail to the right, while negative skewness shows a tail
that stretches left. Understanding skewness can provide insights into potential biases in data and help anticipate
the nature of future data points. It's particularly useful for identifying the likelihood of extreme outcomes in
financial returns, enabling more informed decision-making based on the distribution's shape over a specified period.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 

---
### Comando: `/quantitative/stats/variance`

**Descripción:** Calculate the variance of a target column.

Variance measures the dispersion of a set of data points around their mean. It is a key metric for
assessing the volatility and stability of financial returns or other time series data.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 

---
### Comando: `/quantitative/stats/stdev`

**Descripción:** Calculate the rolling standard deviation of a target column.

Standard deviation is a measure of the amount of variation or dispersion of a set of values.
It is widely used to assess the risk and volatility of financial returns or other time series data
It is the square root of the variance.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 

---
### Comando: `/quantitative/stats/kurtosis`

**Descripción:** Calculate the rolling kurtosis of a target column.

Kurtosis measures the "tailedness" of the probability distribution of a real-valued random variable.
High kurtosis indicates a distribution with heavy tails (outliers), suggesting a higher risk of extreme outcomes.
Low kurtosis indicates a distribution with lighter tails (less outliers), suggesting less risk of extreme outcomes.
This function helps in assessing the risk of outliers in financial returns or other time series data.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 

---
### Comando: `/quantitative/stats/quantile`

**Descripción:** Calculate the quantile of a target column at a specified quantile percentage.

Quantiles are points dividing the range of a probability distribution into intervals with equal probabilities,
or dividing the sample in the same way.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 
  - `--quantile_pct` (Opcional) `[float]`: 

---
### Comando: `/quantitative/stats/mean`

**Descripción:** Calculate the average of a target column.

The rolling mean is a simple moving average that calculates the average of a target variable.
This function is widely used in financial analysis to smooth short-term fluctuations and highlight longer-term trends
or cycles in time series data.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 

---
### Comando: `/quantitative/performance/omega_ratio`

**Descripción:** Calculate the Omega Ratio.

The Omega Ratio is a sophisticated metric that goes beyond traditional performance measures by considering the
probability of achieving returns above a given threshold. It offers a more nuanced view of risk and reward,
focusing on the likelihood of success rather than just average outcomes.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 
  - `--threshold_start` (Opcional) `[float]`: 
  - `--threshold_end` (Opcional) `[float]`: 

---
### Comando: `/quantitative/performance/sharpe_ratio`

**Descripción:** Get Rolling Sharpe Ratio.

This function calculates the Sharpe Ratio, a metric used to assess the return of an investment compared to its risk.
By factoring in the risk-free rate, it helps you understand how much extra return you're getting for the extra
volatility that you endure by holding a riskier asset. The Sharpe Ratio is essential for investors looking to
compare the efficiency of different investments, providing a clear picture of potential rewards in relation to their
risks over a specified period. Ideal for gauging the effectiveness of investment strategies, it offers insights into
optimizing your portfolio for maximum return on risk.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 
  - `--rfr` (Opcional) `[float]`: 
  - `--window` (Opcional) `[int]`: 
  - `--index` (Opcional) `[str]`: 

---
### Comando: `/quantitative/performance/sortino_ratio`

**Descripción:** Get rolling Sortino Ratio.

The Sortino Ratio enhances the evaluation of investment returns by distinguishing harmful volatility
from total volatility. Unlike other metrics that treat all volatility as risk, this command specifically assesses
the volatility of negative returns relative to a target or desired return.
It's particularly useful for investors who are more concerned with downside risk than with overall volatility.
By calculating the Sortino Ratio, investors can better understand the risk-adjusted return of their investments,
focusing on the likelihood and impact of negative returns.
This approach offers a more nuanced tool for portfolio optimization, especially in strategies aiming
to minimize the downside.

For method & terminology see:
http://www.redrockcapital.com/Sortino__A__Sharper__Ratio_Red_Rock_Capital.pdf

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 
  - `--target_return` (Opcional) `[float]`: 
  - `--window` (Opcional) `[int]`: 
  - `--adjusted` (Opcional) `[bool]`: 
  - `--index` (Opcional) `[str]`: 

---
### Comando: `/quantitative/normality`

**Descripción:** Get Normality Statistics.

- **Kurtosis**: whether the kurtosis of a sample differs from the normal distribution.
- **Skewness**: whether the skewness of a sample differs from the normal distribution.
- **Jarque-Bera**: whether the sample data has the skewness and kurtosis matching a normal distribution.
- **Shapiro-Wilk**: whether a random sample comes from a normal distribution.
- **Kolmogorov-Smirnov**: whether two underlying one-dimensional probability distributions differ.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 

---
### Comando: `/quantitative/capm`

**Descripción:** Get Capital Asset Pricing Model (CAPM).

CAPM offers a streamlined way to assess the expected return on an investment while accounting for its risk relative
to the market. It's a cornerstone of modern financial theory that helps investors understand the trade-off between
risk and return, guiding more informed investment choices.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 

---
### Comando: `/quantitative/unitroot_test`

**Descripción:** Get Unit Root Test.

This function applies two renowned tests to assess whether your data series is stationary or if it contains a unit
root, indicating it may be influenced by time-based trends or seasonality. The Augmented Dickey-Fuller (ADF) test
helps identify the presence of a unit root, suggesting that the series could be non-stationary and potentially
unpredictable over time. On the other hand, the Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test checks for the
stationarity of the series, where failing to reject the null hypothesis indicates a stable, stationary series.
Together, these tests provide a comprehensive view of your data's time series properties, essential for
accurate modeling and forecasting.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 
  - `--fuller_reg` (Opcional) `[Literal['c', 'ct', 'ctt', 'nc']]`: 
  - `--kpss_reg` (Opcional) `[Literal['c', 'ct']]`: 

---
### Comando: `/quantitative/summary`

**Descripción:** Get Summary Statistics.

The summary that offers a snapshot of its central tendencies, variability, and distribution.
This command calculates essential statistics, including mean, standard deviation, variance,
and specific percentiles, to provide a detailed profile of your target column. B
y examining these metrics, you gain insights into the data's overall behavior, helping to identify patterns,
outliers, or anomalies. The summary table is an invaluable tool for initial data exploration,
ensuring you have a solid foundation for further analysis or reporting.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` *(Requerido)* `[str]`: 

---
### Comando: `/regulators/sec/filing_headers`

**Descripción:** Download the index headers, and cover page if available, for any SEC filing.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `sec`:*
  - `--url` (Opcional) `[str | None]`: URL for the SEC filing. The specific URL is not directly used or downloaded, but is used to generate the base URL for the filing. e.g. https://www.sec.gov/Archives/edgar/data/317540/000031754024000045/coke-20240731.htm and https://www.sec.gov/Archives/edgar/data/317540/000031754024000045/ are both valid URLs for the same filing.
  - `--use_cache` (Opcional) `[bool | None]`: Use cache for the index headers and cover page. Default is True.

---
### Comando: `/regulators/sec/htm_file`

**Descripción:** Download a raw HTML object from the SEC website.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `sec`:*
  - `--url` (Opcional) `[str | None]`: URL for the SEC filing.
  - `--use_cache` (Opcional) `[bool | None]`: Cache the file for use later. Default is True.

---
### Comando: `/regulators/sec/cik_map`

**Descripción:** Map a ticker symbol to a CIK number.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**
  - `--symbol` *(Requerido)* `[str]`: Symbol to get data for.

  *Exclusivos del proveedor `sec`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether or not to use cache for the request, default is True.

---
### Comando: `/regulators/sec/institutions_search`

**Descripción:** Search SEC-regulated institutions by name and return a list of results with CIK numbers.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**
  - `--query` (Opcional) `[str | None]`: Search query.

  *Exclusivos del proveedor `sec`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether or not to use cache.

---
### Comando: `/regulators/sec/schema_files`

**Descripción:** Use tool for navigating the directory of SEC XML schema files by year.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**
  - `--query` (Opcional) `[str | None]`: Search query.

  *Exclusivos del proveedor `sec`:*
  - `--url` (Opcional) `[str | None]`: Enter an optional URL path to fetch the next level.
  - `--use_cache` (Opcional) `[bool | None]`: Whether or not to use cache.

---
### Comando: `/regulators/sec/symbol_map`

**Descripción:** Map a CIK number to a ticker symbol, leading 0s can be omitted or included.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**
  - `--query` *(Requerido)* `[str]`: Search query.
  - `--use_cache` (Opcional) `[bool | None]`: Whether or not to use cache. If True, cache will store for seven days.

  *Exclusivos del proveedor `sec`:*

---
### Comando: `/regulators/sec/rss_litigation`

**Descripción:** Get the RSS feed that provides links to litigation releases concerning civil lawsuits brought by the Commission in federal court.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `sec`:*

---
### Comando: `/regulators/sec/sic_search`

**Descripción:** Search for Industry Titles, Reporting Office, and SIC Codes. An empty query string returns all results.

- **Proveedores disponibles / soportados:** `sec`

**Flags / Parámetros (Standard & Providers):**
  - `--query` (Opcional) `[str | None]`: Search query.

  *Exclusivos del proveedor `sec`:*
  - `--use_cache` (Opcional) `[bool | None]`: Whether or not to use cache.

---
### Comando: `/regulators/cftc/cot_search`

**Descripción:** Get the current Commitment of Traders Reports.

Search a list of the current Commitment of Traders Reports series information.

- **Proveedores disponibles / soportados:** `cftc`

**Flags / Parámetros (Standard & Providers):**
  - `--query` (Opcional) `[str | None]`: Search query.

  *Exclusivos del proveedor `cftc`:*

---
### Comando: `/regulators/cftc/cot`

**Descripción:** Get Commitment of Traders Reports.

- **Proveedores disponibles / soportados:** `cftc`

**Flags / Parámetros (Standard & Providers):**
  - `--id` (Opcional) `[str | None]`: A string with the CFTC market code or other identifying string, such as the contract market name, commodity name, or commodity group - i.e, 'gold' or 'japanese yen'.Default report is Fed Funds Futures. Use the 'cftc_market_code' for an exact match.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format. Default is the most recent report.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format.

  *Exclusivos del proveedor `cftc`:*
  - `--report_type` (Opcional) `[Literal['legacy', 'disaggregated', 'financial', 'supplemental'] | None]`: The type of report to retrieve. Set `id` as 'all' to return all items in the report             type (default date range returns the latest report). The Legacy report is broken down by exchange             with reported open interest further broken down into three trader classifications: commercial,             non-commercial and non-reportable. The Disaggregated reports are broken down by Agriculture and             Natural Resource contracts. The Disaggregated reports break down reportable open interest positions             into four classifications: Producer/Merchant, Swap Dealers, Managed Money and Other Reportables.             The Traders in Financial Futures (TFF) report includes financial contracts. The TFF report breaks             down the reported open interest into five classifications: Dealer, Asset Manager, Leveraged Money,             Other Reportables and Non-Reportables.
  - `--futures_only` (Opcional) `[bool | None]`: Returns the futures-only report. Default is False, for the combined report.

---
### Comando: `/technical/relative_rotation`

**Descripción:** Calculate the Relative Strength Ratio and Relative Strength Momentum for a group of symbols against a benchmark.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--benchmark` *(Requerido)* `[str]`: 
  - `--study` (Opcional) `[Literal['price', 'volume', 'volatility']]`: 
  - `--long_period` (Opcional) `[int | None]`: 
  - `--short_period` (Opcional) `[int | None]`: 
  - `--window` (Opcional) `[int | None]`: 
  - `--trading_periods` (Opcional) `[int | None]`: 
  - `--chart_params` (Opcional) `[dict[str, Any] | None]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/technical/atr`

**Descripción:** Calculate the Average True Range.

Used to measure volatility, especially volatility caused by gaps or limit moves.
The ATR metric helps understand how much the values in your data change on average,
giving insights into the stability or unpredictability during a certain period.
It's particularly useful for spotting trends of increase or decrease in variations,
without getting into technical trading details.
The method considers not just the day-to-day changes but also accounts for any
sudden jumps or drops, ensuring you get a comprehensive view of movement.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--mamode` (Opcional) `[Literal['rma', 'ema', 'sma', 'wma']]`: 
  - `--drift` (Opcional) `[int]`: 
  - `--offset` (Opcional) `[int]`: 

---
### Comando: `/technical/fib`

**Descripción:** Create Fibonacci Retracement Levels.

This method draws from a classic technique to pinpoint significant price levels
that often indicate where the market might find support or resistance.
It's a tool used to gauge potential turning points in the data by applying a
mathematical approach rooted in nature's patterns. Is used to get insights into
where prices could head next, based on historical movements.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--close_column` (Opcional) `[Literal['close', 'adj_close']]`: 
  - `--period` (Opcional) `[int]`: 
  - `--start_date` (Opcional) `[str | None]`: 
  - `--end_date` (Opcional) `[str | None]`: 

---
### Comando: `/technical/obv`

**Descripción:** Calculate the On Balance Volume (OBV).

Is a cumulative total of the up and down volume. When the close is higher than the
previous close, the volume is added to the running total, and when the close is
lower than the previous close, the volume is subtracted from the running total.

To interpret the OBV, look for the OBV to move with the price or precede price moves.
If the price moves before the OBV, then it is a non-confirmed move. A series of rising peaks,
or falling troughs, in the OBV indicates a strong trend. If the OBV is flat, then the market
is not trending.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--offset` (Opcional) `[int]`: 

---
### Comando: `/technical/fisher`

**Descripción:** Perform the Fisher Transform.

A technical indicator created by John F. Ehlers that converts prices into a Gaussian
normal distribution. The indicator highlights when prices have moved to an extreme,
based on recent prices.
This may help in spotting turning points in the price of an asset. It also helps
show the trend and isolate the price waves within a trend.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--signal` (Opcional) `[int]`: 

---
### Comando: `/technical/adosc`

**Descripción:** Calculate the Accumulation/Distribution Oscillator.

Also known as the Chaikin Oscillator.

Essentially a momentum indicator, but of the Accumulation-Distribution line
rather than merely price. It looks at both the strength of price moves and the
underlying buying and selling pressure during a given time period. The oscillator
reading above zero indicates net buying pressure, while one below zero registers
net selling pressure. Divergence between the indicator and pure price moves are
the most common signals from the indicator, and often flag market turning points.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--fast` (Opcional) `[int]`: 
  - `--slow` (Opcional) `[int]`: 
  - `--offset` (Opcional) `[int]`: 

---
### Comando: `/technical/bbands`

**Descripción:** Calculate the Bollinger Bands.

Consist of three lines. The middle band is a simple moving average (generally 20
periods) of the typical price (TP). The upper and lower bands are F standard
deviations (generally 2) above and below the middle band.
The bands widen and narrow when the volatility of the price is higher or lower,
respectively.

Bollinger Bands do not, in themselves, generate buy or sell signals;
they are an indicator of overbought or oversold conditions. When the price is near the
upper or lower band it indicates that a reversal may be imminent. The middle band
becomes a support or resistance level. The upper and lower bands can also be
interpreted as price targets. When the price bounces off of the lower band and crosses
the middle band, then the upper band becomes the price target.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` (Opcional) `[str]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--std` (Opcional) `[float]`: 
  - `--mamode` (Opcional) `[Literal['sma', 'ema', 'wma', 'rma']]`: 
  - `--offset` (Opcional) `[int]`: 

---
### Comando: `/technical/zlma`

**Descripción:** Calculate the zero lag exponential moving average (ZLEMA).

Created by John Ehlers and Ric Way. The idea is do a
regular exponential moving average (EMA) calculation but
on a de-lagged data instead of doing it on the regular data.
Data is de-lagged by removing the data from "lag" days ago
thus removing (or attempting to) the cumulative effect of
the moving average.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` (Opcional) `[str]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--offset` (Opcional) `[int]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/technical/aroon`

**Descripción:** Calculate the Aroon Indicator.

The word aroon is Sanskrit for "dawn's early light." The Aroon
indicator attempts to show when a new trend is dawning. The indicator consists
of two lines (Up and Down) that measure how long it has been since the highest
high/lowest low has occurred within an n period range.

When the Aroon Up is staying between 70 and 100 then it indicates an upward trend.
When the Aroon Down is staying between 70 and 100 then it indicates an downward trend.
A strong upward trend is indicated when the Aroon Up is above 70 while the Aroon Down is below 30.
Likewise, a strong downward trend is indicated when the Aroon Down is above 70 while
the Aroon Up is below 30. Also look for crossovers. When the Aroon Down crosses above
the Aroon Up, it indicates a weakening of the upward trend (and vice versa).

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--scalar` (Opcional) `[float]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/technical/sma`

**Descripción:** Calculate the Simple Moving Average (SMA).

Moving Averages are used to smooth the data in an array to
help eliminate noise and identify trends. The Simple Moving Average is literally
the simplest form of a moving average. Each output value is the average of the
previous n values. In a Simple Moving Average, each value in the time period carries
equal weight, and values outside of the time period are not included in the average.
This makes it less responsive to recent changes in the data, which can be useful for
filtering out those changes.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` (Opcional) `[str]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--offset` (Opcional) `[int]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/technical/demark`

**Descripción:** Calculate the Demark sequential indicator.

This indicator offers a strategic way to spot potential reversals in market trends.
It's designed to highlight moments when the current trend may be running out of steam,
suggesting a possible shift in direction. By focusing on specific patterns in price movements, it provides
valuable insights for making informed decisions on future changes and identifies trend exhaustion points
with precision.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--target` (Opcional) `[str]`: 
  - `--show_all` (Opcional) `[bool]`: 
  - `--asint` (Opcional) `[bool]`: 
  - `--offset` (Opcional) `[int]`: 

---
### Comando: `/technical/vwap`

**Descripción:** Calculate the Volume Weighted Average Price (VWAP).

Measures the average typical price by volume.
It is typically used with intraday charts to identify general direction.
It helps to understand the true average price factoring in the volume of transactions,
and serves as a benchmark for assessing the market's direction over short periods, such as a single trading day.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--anchor` (Opcional) `[str]`: 
  - `--offset` (Opcional) `[int]`: 

---
### Comando: `/technical/macd`

**Descripción:** Calculate the Moving Average Convergence Divergence (MACD).

Difference between two Exponential Moving Averages. The Signal line is an
Exponential Moving Average of the MACD.

The MACD signals trend changes and indicates the start of new trend direction.
High values indicate overbought conditions, low values indicate oversold conditions.
Divergence with the price indicates an end to the current trend, especially if the
MACD is at extreme high or low values. When the MACD line crosses above the
signal line a buy signal is generated. When the MACD crosses below the signal line a
sell signal is generated. To confirm the signal, the MACD should be above zero for a buy,
and below zero for a sell.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` (Opcional) `[str]`: 
  - `--index` (Opcional) `[str]`: 
  - `--fast` (Opcional) `[int]`: 
  - `--slow` (Opcional) `[int]`: 
  - `--signal` (Opcional) `[int]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/technical/hma`

**Descripción:** Calculate the Hull Moving Average (HMA).

Solves the age old dilemma of making a moving average more responsive to current
price activity whilst maintaining curve smoothness.
In fact the HMA almost eliminates lag altogether and manages to improve smoothing
at the same time.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` (Opcional) `[str]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--offset` (Opcional) `[int]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/technical/donchian`

**Descripción:** Calculate the Donchian Channels.

Three lines generated by moving average calculations that comprise an indicator
formed by upper and lower bands around a midrange or median band. The upper band
marks the highest price of a security over N periods while the lower band
marks the lowest price of a security over N periods. The area
between the upper and lower bands represents the Donchian Channel.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--lower_length` (Opcional) `[int]`: 
  - `--upper_length` (Opcional) `[int]`: 
  - `--offset` (Opcional) `[int]`: 

---
### Comando: `/technical/ichimoku`

**Descripción:** Calculate the Ichimoku Cloud.

Also known as Ichimoku Kinko Hyo, is a versatile indicator that defines support and
resistance, identifies trend direction, gauges momentum and provides trading
signals. Ichimoku Kinko Hyo translates into "one look equilibrium chart". With
one look, chartists can identify the trend and look for potential signals within
that trend.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--conversion` (Opcional) `[int]`: 
  - `--base` (Opcional) `[int]`: 
  - `--lagging` (Opcional) `[int]`: 
  - `--offset` (Opcional) `[int]`: 
  - `--lookahead` (Opcional) `[bool]`: 

---
### Comando: `/technical/clenow`

**Descripción:** Calculate the Clenow Volatility Adjusted Momentum.

The Clenow Volatility Adjusted Momentum is a sophisticated approach to understanding market momentum with a twist.
It adjusts for volatility, offering a clearer picture of true momentum by considering how price movements are
influenced by their volatility over a set period. It helps in identifying stronger, more reliable trends.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--target` (Opcional) `[str]`: 
  - `--period` (Opcional) `[int]`: 

---
### Comando: `/technical/ad`

**Descripción:** Calculate the Accumulation/Distribution Line.

Similar to the On Balance Volume (OBV).
Sums the volume times +1/-1 based on whether the close is higher than the previous
close. The Accumulation/Distribution indicator, however multiplies the volume by the
close location value (CLV). The CLV is based on the movement of the issue within a
single bar and can be +1, -1 or zero.


The Accumulation/Distribution Line is interpreted by looking for a divergence in
the direction of the indicator relative to price. If the Accumulation/Distribution
Line is trending upward it indicates that the price may follow. Also, if the
Accumulation/Distribution Line becomes flat while the price is still rising (or falling)
then it signals an impending flattening of the price.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--offset` (Opcional) `[int]`: 

---
### Comando: `/technical/adx`

**Descripción:** Calculate the Average Directional Index (ADX).

The ADX is a Welles Wilder style moving average of the Directional Movement Index (DX).
The values range from 0 to 100, but rarely get above 60. To interpret the ADX, consider
a high number to be a strong trend, and a low number, a weak trend.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--scalar` (Opcional) `[float]`: 
  - `--drift` (Opcional) `[int]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/technical/wma`

**Descripción:** Calculate the Weighted Moving Average (WMA).

A Weighted Moving Average puts more weight on recent data and less on past data.
This is done by multiplying each bar's price by a weighting factor. Because of its
unique calculation, WMA will follow prices more closely than a corresponding Simple
Moving Average.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` (Opcional) `[str]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--offset` (Opcional) `[int]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/technical/cci`

**Descripción:** Calculate the Commodity Channel Index (CCI).

The CCI is designed to detect beginning and ending market trends.
The range of 100 to -100 is the normal trading range. CCI values outside of this
range indicate overbought or oversold conditions. You can also look for price
divergence in the CCI. If the price is making new highs, and the CCI is not,
then a price correction is likely.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--scalar` (Opcional) `[float]`: 

---
### Comando: `/technical/rsi`

**Descripción:** Calculate the Relative Strength Index (RSI).

RSI calculates a ratio of the recent upward price movements to the absolute price
movement. The RSI ranges from 0 to 100.
The RSI is interpreted as an overbought/oversold indicator when
the value is over 70/below 30. You can also look for divergence with price. If
the price is making new highs/lows, and the RSI is not, it indicates a reversal.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` (Opcional) `[str]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--scalar` (Opcional) `[float]`: 
  - `--drift` (Opcional) `[int]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/technical/stoch`

**Descripción:** Calculate the Stochastic Oscillator.

The Stochastic Oscillator measures where the close is in relation
to the recent trading range. The values range from zero to 100. %D values over 75
indicate an overbought condition; values under 25 indicate an oversold condition.
When the Fast %D crosses above the Slow %D, it is a buy signal; when it crosses
below, it is a sell signal. The Raw %K is generally considered too erratic to use
for crossover signals.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--fast_k_period` (Opcional) `[int]`: 
  - `--slow_d_period` (Opcional) `[int]`: 
  - `--slow_k_period` (Opcional) `[int]`: 

---
### Comando: `/technical/kc`

**Descripción:** Calculate the Keltner Channels.

Keltner Channels are volatility-based bands that are placed
on either side of an asset's price and can aid in determining
the direction of a trend.The Keltner channel uses the average
true range (ATR) or volatility, with breaks above or below the top
and bottom barriers signaling a continuation.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--scalar` (Opcional) `[float]`: 
  - `--mamode` (Opcional) `[Literal['ema', 'sma', 'wma', 'hma', 'zlma']]`: 
  - `--offset` (Opcional) `[int]`: 

---
### Comando: `/technical/cg`

**Descripción:** Calculate the Center of Gravity.

The Center of Gravity indicator, in short, is used to anticipate future price movements
and to trade on price reversals as soon as they happen. However, just like other oscillators,
the COG indicator returns the best results in range-bound markets and should be avoided when
the price is trending. Traders who use it will be able to closely speculate the upcoming
price change of the asset.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 

---
### Comando: `/technical/cones`

**Descripción:** Calculate the realized volatility quantiles over rolling windows of time.

The cones indicator is designed to map out the ebb and flow of price movements through a detailed analysis of
volatility quantiles. By examining the range of volatility within specific time frames, it offers a nuanced view of
market behavior, highlighting periods of stability and turbulence.

The model for calculating volatility is selectable and can be one of the following:
- Standard deviation
- Parkinson
- Garman-Klass
- Hodges-Tompkins
- Rogers-Satchell
- Yang-Zhang

Read more about it in the model parameter description.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--index` (Opcional) `[str]`: 
  - `--lower_q` (Opcional) `[float]`: 
  - `--upper_q` (Opcional) `[float]`: 
  - `--model` (Opcional) `[Literal['std', 'parkinson', 'garman_klass', 'hodges_tompkins', 'rogers_satchell', 'yang_zhang']]`: 
  - `--is_crypto` (Opcional) `[bool]`: 
  - `--trading_periods` (Opcional) `[int | None]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/technical/ema`

**Descripción:** Calculate the Exponential Moving Average (EMA).

EMA is a cumulative calculation, including all data. Past values have
a diminishing contribution to the average, while more recent values have a greater
contribution. This method allows the moving average to be more responsive to changes
in the data.

**Flags / Parámetros (Standard & Providers):**
  - `--data` *(Requerido)* `[ForwardRef('Data') | ForwardRef('DataFrame') | ForwardRef('Series') | ForwardRef('ndarray') | dict | list]`: 
  - `--target` (Opcional) `[str]`: 
  - `--index` (Opcional) `[str]`: 
  - `--length` (Opcional) `[int]`: 
  - `--offset` (Opcional) `[int]`: 
  - `--chart` (Opcional) `[bool]`: 

---
### Comando: `/uscongress/bills`

**Descripción:** Get and filter lists of Congressional Bills.

- **Proveedores disponibles / soportados:** `congress_gov`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `congress_gov`:*
  - `--congress` (Opcional) `[int | None]`: Congress number (e.g., 118 for the 118th Congress). The 103rd Congress started in 1993, which is the earliest date supporting full text versions. Each Congress spans two years, starting in odd-numbered years.
  - `--bill_type` (Opcional) `[str | None]`: Bill type (e.g., 'hr' for House bills).  Must be one of: hr, s, hjres, sjres, hconres, sconres, hres, sres.  Bills -----  A bill is the form used for most legislation, whether permanent or temporary, general or special, public or private.  A bill originating in the House of Representatives is designated by the letters “H.R.”, signifying “House of Representatives”, followed by a number that it retains throughout all its parliamentary stages.  Bills are presented to the President for action when approved in identical form by both the House of Representatives and the Senate.  Joint Resolutions -----------------  Joint resolutions may originate either in the House of Representatives or in the Senate.  There is little practical difference between a bill and a joint resolution. Both are subject to the same procedure, except for a joint resolution proposing an amendment to the Constitution.  On approval of such a resolution by two-thirds of both the House and Senate, it is sent directly to the Administrator of General Services for submission to the individual states for ratification.  It is not presented to the President for approval. A joint resolution originating in the House of Representatives is designated “H.J.Res.” followed by its individual number. Joint resolutions become law in the same manner as bills.  Concurrent Resolutions ----------------------  Matters affecting the operations of both the House of Representatives and Senate are usually initiated by means of concurrent resolutions.  A concurrent resolution originating in the House of Representatives is designated “H.Con.Res.” followed by its individual number.  On approval by both the House of Representatives and Senate, they are signed by the Clerk of the House and the Secretary of the Senate.  They are not presented to the President for action.  Simple Resolutions ------------------  A matter concerning the operation of either the House of Representatives or Senate alone is initiated by a simple resolution.  A resolution affecting the House of Representatives is designated “H.Res.” followed by its number.  They are not presented to the President for action.
  - `--start_date` (Opcional) `[date | None | str]`: Start date of the data, in YYYY-MM-DD format. Filters bills by the last updated date.
  - `--end_date` (Opcional) `[date | None | str]`: End date of the data, in YYYY-MM-DD format. Filters bills by the last updated date.
  - `--limit` (Opcional) `[int | None]`: The number of data entries to return. When None, default sets to 100 (max 250). Set to 0 for no limit (must be used with 'bill_type' and 'congress'). Setting to 0 will nullify the start_date, end_date, and offset parameters.
  - `--offset` (Opcional) `[int | None]`: The starting record returned. 0 is the first record.
  - `--sort_by` (Opcional) `[Literal['asc', 'desc'] | None]`: Sort by update date. Default is latest first.

---
### Comando: `/uscongress/bill_text_urls`

**Descripción:** Get document choices for a specific bill.

This function is used by the Congressional Bills Viewer widget, in OpenBB Workspace,
to populate PDF document choices for the selected bill.

When 'is_workspace' is False (default), it returns a list of the available text versions
of the specified bill and their download links for the different formats.

**Flags / Parámetros (Standard & Providers):**
  - `--bill_url` *(Requerido)* `[str]`: 
  - `--is_workspace` (Opcional) `[bool]`: 
  - `--provider` (Opcional) `[str | None]`: 

---
### Comando: `/uscongress/bill_info`

**Descripción:** Get summary, status, and other metadata for a specific bill.

Enter the URL of the bill as: https://api.congress.gov/v3/bill/119/hr/131?

URLs for bills can be found from the `uscongress.bills` endpoint.

The raw JSON response from the API will be returned along with a formatted
text version of the key information from the raw response.

In OpenBB Workspace, this command returns as a Markdown widget.

- **Proveedores disponibles / soportados:** `congress_gov`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `congress_gov`:*
  - `--bill_url` *(Requerido)* `[str]`: Enter a base URL of a bill (e.g., 'https://api.congress.gov/v3/bill/119/s/1947?format=json'). Alternatively, you can enter a bill number (e.g., '119/s/1947').

---
### Comando: `/uscongress/bill_text`

**Descripción:** Download the content of bill(s) from a Congress.gov file.

Note: This endpoint returns only the results array of the OBBject.

Enter a list of URLs to download the bill text.

For the API, the body of the request will look like this:

```json
{
"urls": [
"https://www.congress.gov/119/bills/hr1/BILLS-119hr1eh.pdf"
]
}
```

In OpenBB Workspace, this command returns as a multi-file viewer widget.

- **Proveedores disponibles / soportados:** `congress_gov`

**Flags / Parámetros (Standard & Providers):**

  *Exclusivos del proveedor `congress_gov`:*
  - `--urls` *(Requerido)* `[str | list[str] | dict[str, list[str]]]`: list of direct bill URLs to download.

---
