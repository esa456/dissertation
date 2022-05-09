#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:56:24 2018

@author: Esa
"""




# use natural language toolkit
import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
stemmer = LancasterStemmer()

# 2 classes of training data
training_data = []
training_data.append({"class":"related", "sentence":"""Post-it maker 3M's quarterly profit rises 3.8%"""})
training_data.append({"class":"related", "sentence":"""Post-it notes maker 3M's quarterly profit rises 11.3%"""})
training_data.append({"class":"related", "sentence":"""Post-it maker 3M trims forecasts for second time"""})
training_data.append({"class":"related", "sentence":"""Post-it maker 3M trims forecasts for second time"""})
training_data.append({"class":"related", "sentence":"""Post-it notes maker 3M's profit beats estimates on lower costs"""})
training_data.append({"class":"related", "sentence":"""Lower costs help 3M profit top estimates"""})
training_data.append({"class":"related", "sentence":"""3M tops Street third-quarter forecasts"""})
training_data.append({"class":"related", "sentence":"""3M misses Street 2Q forecasts"""})
training_data.append({"class":"related", "sentence":"""3M misses Street 2Q forecasts"""})
training_data.append({"class":"related", "sentence":"""American Express falls 1% despite earnings beat"""})
training_data.append({"class":"related", "sentence":"""American Express pops 5% on earnings beat"""})
training_data.append({"class":"related", "sentence":"""American Express pops on earnings beat"""})
training_data.append({"class":"related", "sentence":"""American Express beats on top and bottom line"""})
training_data.append({"class":"related", "sentence":"""AmEx dips after company says it will temporarily suspend buybacks due to tax law"""})
training_data.append({"class":"related", "sentence":"""AmEx raises full-year forecast, says CEO will leave Feb. 1"""})
training_data.append({"class":"related", "sentence":"""AmEx profits, revenue exceed analyst estimates"""})
training_data.append({"class":"related", "sentence":"""Apple said it wants to become 'cash neutral' — which could be a huge boost for earnings"""})
training_data.append({"class":"related", "sentence":"""Apple stock pops despite falling iPhone shipments and weak guidance"""})
training_data.append({"class":"related", "sentence":"""Apple falls 2% as it posts 3rd straight quarter of year-on-year revenue declines"""})
training_data.append({"class":"related", "sentence":"""Apple sold fewer iPhones than a year ago"""})
training_data.append({"class":"related", "sentence":"""Apple downgraded by BMO, expects iPhone maker to slash revenue forecast this week"""})
training_data.append({"class":"related", "sentence":"""Apple could be the best of the bunch in this tech earnings avalanche"""})
training_data.append({"class":"related", "sentence":"""Apple is testing key support levels ahead of earnings this week"""})
training_data.append({"class":"related", "sentence":"""Here's why Cramer says he's had it with analysts after Apple's earnings call"""})
training_data.append({"class":"related", "sentence":"""Cramer defends Apple after rare downgrade, saying Q4 earnings call 'directly contradicts' report"""})
training_data.append({"class":"related", "sentence":"""Apple blows past Wall Street expectations as the iPhone 8 becomes a surprise best-seller"""})
training_data.append({"class":"related", "sentence":"""Apple earnings leave shareholders bullish, investors wary"""})
training_data.append({"class":"related", "sentence":"""Apple earnings could be a ‘sell the news’ event"""})
training_data.append({"class":"related", "sentence":"""Apple jumps more than 6%, set to open at record high after earnings beat estimates"""})
training_data.append({"class":"related", "sentence":"""Tim Cook on Apple's big earnings beat"""})
training_data.append({"class":"related", "sentence":"""Apple cash pile hits new record of $261.5 billion"""})
training_data.append({"class":"related", "sentence":"""Wall Street doesn't really care how much money Apple is making right now"""})
training_data.append({"class":"related", "sentence":"""Apple hits record $775 billion in market cap before disappointing earnings"""})
training_data.append({"class":"related", "sentence":"""Apple misses on iPhone shipments, stock drops"""})
training_data.append({"class":"related", "sentence":"""Tim Cook explains how Apple will double its fastest growing business by 2020"""})
training_data.append({"class":"related", "sentence":"""Apple shares pop 4% after big earnings beat, record revenues"""})
training_data.append({"class":"related", "sentence":"""Here's why Cramer says he's had it with analysts after Apple's earnings call"""})
training_data.append({"class":"related", "sentence":"""Apple earnings leave shareholders bullish, investors wary"""})
training_data.append({"class":"related", "sentence":"""Top analyst downgrades Apple on 'weaker-than-expected' sales and profit margin guidance"""})
training_data.append({"class":"related", "sentence":"""Apple drags Dow lower after earnings, loses more than $14 billion in market cap"""})
training_data.append({"class":"related", "sentence":"""Top analyst downgrades Apple on 'weaker-than-expected' sales and profit margin guidance"""})
training_data.append({"class":"related", "sentence":"""Apple drags Dow lower after earnings, loses more than $14 billion in market cap"""})
training_data.append({"class":"related", "sentence":"""Apple falls 2% as it posts 3rd straight quarter of year-on-year revenue declines"""})
training_data.append({"class":"related", "sentence":"""Apple does it again: Stock climbs 6% as bet on iPhone SE pays off"""})
training_data.append({"class":"related", "sentence":"""Investors are bracing for Apple to do something it hasn't since 2012"""})
training_data.append({"class":"related", "sentence":"""Apple plunges after earnings, wiping out $46B in market cap"""})
training_data.append({"class":"related", "sentence":"""Apple revenue, iPhone sales come up short"""})
training_data.append({"class":"related", "sentence":"""Boeing misses earnings estimates; beats on revenues"""})
training_data.append({"class":"related", "sentence":"""Boeing shares sink after gloomy 2016 forecast"""})
training_data.append({"class":"related", "sentence":"""Boeing to make just six 747-8 jumbos a year"""})
training_data.append({"class":"related", "sentence":"""Boeing stock hits all-time high after the company says it expects to crush record jet deliveries"""})
training_data.append({"class":"related", "sentence":"""Boeing stock drops over 3% after earnings, dragging down Dow"""})
training_data.append({"class":"related", "sentence":"""Boeing shares soar after 2nd-quarter profit, cash top estimates"""})
training_data.append({"class":"related", "sentence":"""Boeing shares soar after 2nd-quarter profit, cash top estimates"""})
training_data.append({"class":"related", "sentence":"""Boeing profit rises 19%"""})
training_data.append({"class":"related", "sentence":"""Boeing expects to deliver more planes in 2017"""})
training_data.append({"class":"related", "sentence":"""Boeing profit jumps; raises delivery and revenue outlook"""})
training_data.append({"class":"related", "sentence":"""Boeing profit jumps; raises delivery and revenue outlook"""})
training_data.append({"class":"related", "sentence":"""Boeing posts lower-than-expected loss, stock jumps"""})
training_data.append({"class":"related", "sentence":"""Boeing will take $2.05 billion in charges for second-quarter earnings"""})
training_data.append({"class":"related", "sentence":"""Caterpillar cuts Q1 earnings, revenue guidance"""})
training_data.append({"class":"related", "sentence":"""Caterpillar CEO expects another 'rough' year"""})
training_data.append({"class":"related", "sentence":"""Caterpillar shares jump after earnings, revenue easily top estimates"""})
training_data.append({"class":"related", "sentence":"""Caterpillar shares soar more than 7% on strong earnings beat and yet another raised forecast"""})
training_data.append({"class":"related", "sentence":"""Shares of Caterpillar jump 5% on second-quarter earnings beat"""})
training_data.append({"class":"related", "sentence":"""Caterpillar smashes expectations, raises forecast; shares jump"""})
training_data.append({"class":"related", "sentence":"""Caterpillar revenue and guidance fall short as earnings handily beat estimates"""})
training_data.append({"class":"related", "sentence":"""Caterpillar profit beats but revenue misses in challenging construction environment"""})
training_data.append({"class":"related", "sentence":"""Caterpillar profit beats but revenue misses in challenging construction environment"""})
training_data.append({"class":"related", "sentence":"""Caterpillar shares slump on machinery sales declines"""})
training_data.append({"class":"related", "sentence":"""Caterpillar drives past estimates, brings in stronger earnings than expected"""})
training_data.append({"class":"related", "sentence":"""Caterpillar CEO: 'We're close to the bottom'"""})
training_data.append({"class":"related", "sentence":"""Shares of Caterpillar jump 5% on second-quarter earnings beat"""})
training_data.append({"class":"related", "sentence":"""Chevron signals more asset sales, higher US drilling after missing profit forecasts badly"""})
training_data.append({"class":"related", "sentence":"""Chevron turns in a quarter that trounces Wall Street's expectations"""})
training_data.append({"class":"related", "sentence":"""Chevron to rally 16% despite earnings loss, says Piper Jaffray"""})
training_data.append({"class":"related", "sentence":"""Chevron earnings surprise with loss on $2.8 billion in charges"""})
training_data.append({"class":"related", "sentence":"""Chevron shares slide as oil company misses earnings estimates"""})
training_data.append({"class":"related", "sentence":"""Shares of Chevron fall after the oil major reports its US output declined in third quarter"""})
training_data.append({"class":"related", "sentence":"""Chevron shares rise after profits and revenues beat expectations"""})
training_data.append({"class":"related", "sentence":"""Chevron shares jump about 2% on strong earnings beat"""})
training_data.append({"class":"related", "sentence":"""Cisco CEO talks up prospects after outlook warning slams the stock"""})
training_data.append({"class":"related", "sentence":"""Cisco shares pop 5% on earnings beat, positive guidance"""})
training_data.append({"class":"related", "sentence":"""Cisco CEO: Executing well despite macro slowdown"""})
training_data.append({"class":"related", "sentence":"""Cisco returns to growth, stock pops"""})
training_data.append({"class":"related", "sentence":"""Cisco slides after revenue beat"""})
training_data.append({"class":"related", "sentence":"""Coca-Cola's earnings, sales top Wall Street expectations with more healthy drinks on tap"""})
training_data.append({"class":"related", "sentence":"""Coca-Cola's earnings, sales top Wall Street expectations with more healthy drinks on tap"""})
training_data.append({"class":"related", "sentence":"""Coca-Cola's profit plunges 20 percent on bottling refranchising costs"""})
training_data.append({"class":"related", "sentence":"""Coca-Cola guidance falls short, while earnings meet estimates and revenue beats"""})
training_data.append({"class":"related", "sentence":"""Coca-Cola beats earnings estimates, but net revenue falls"""})
training_data.append({"class":"related", "sentence":"""Coca-Cola beats earnings estimates, but net revenue falls"""})
training_data.append({"class":"related", "sentence":"""Coca-Cola beats on earnings, but cuts revenue forecast"""})
training_data.append({"class":"related", "sentence":"""Coca-Cola sales fall on strong dollar, weak demand"""})
training_data.append({"class":"related", "sentence":"""Coca-Cola beats earnings, as Coke Zero and other new drinks offset flat volume"""})
training_data.append({"class":"related", "sentence":"""Coca-Cola tops estimates, backs full-year outlook"""})
training_data.append({"class":"related", "sentence":"""ESPN is a double-edged sword for Disney as consumers cut the cord"""})
training_data.append({"class":"related", "sentence":"""Disney rises after earnings beat, announces price of ESPN streaming service"""})
training_data.append({"class":"related", "sentence":"""Disney sees worst day in more than a year as ESPN issues drag cable business"""})
training_data.append({"class":"related", "sentence":"""DuPont beats on strong demand in agriculture business"""})
training_data.append({"class":"related", "sentence":"""DuPont reports lower quarterly profit on Dow deal charges"""})
training_data.append({"class":"related", "sentence":"""DuPont reports quarterly profit vs. year-earlier loss"""})
training_data.append({"class":"related", "sentence":"""Cramer: Here's why it's a remarkable quarter for Procter & Gamble and DuPont"""})
training_data.append({"class":"related", "sentence":"""Cramer: Here's why it's a remarkable quarter for Procter & Gamble and DuPont"""})
training_data.append({"class":"related", "sentence":"""DuPont profit beats as cost cuts take hold"""})
training_data.append({"class":"related", "sentence":"""DuPont profit rises 8.5 percent as costs fall"""})
training_data.append({"class":"related", "sentence":"""DuPont raises full-year outlook, Q1 results beat forecast"""})
training_data.append({"class":"related", "sentence":"""DuPont forecasts higher 2016 earnings"""})
training_data.append({"class":"related", "sentence":"""Chemicals giant DowDuPont is upbeat on growth as sales rise 14%"""})
training_data.append({"class":"related", "sentence":"""Exxon Mobil beats expectations for profits and revenue, even as Harvey takes a bite out of earnings"""})
training_data.append({"class":"related", "sentence":"""Exxon Mobil shares drop 2% as profits double, but still fall short of Street expectations"""})
training_data.append({"class":"related", "sentence":"""Exxon Mobil beats earnings expectations as profits more than double from last year"""})
training_data.append({"class":"related", "sentence":"""Exxon Mobil profit and revenue rise as the oil giant takes $2 billion impairment"""})
training_data.append({"class":"related", "sentence":"""Exxon Mobil earnings beat estimates, but fall $1.6 billion from a year ago"""})
training_data.append({"class":"related", "sentence":"""Exxon Mobil shares slide nearly 6% as oil giant's fourth-quarter earnings fall short"""})
training_data.append({"class":"related", "sentence":"""General Electric reveals SEC investigation into accounting"""})
training_data.append({"class":"related", "sentence":"""General Electric falls short in fourth quarter but offers stronger 2018 outlook"""})
training_data.append({"class":"related", "sentence":"""General Electric shares fall 1% after earnings beat Street's expectations"""})
training_data.append({"class":"related", "sentence":"""General Electric shares drop after revenue falls short of expectations"""})
training_data.append({"class":"related", "sentence":"""Goldman Sachs smashes estimates on post-Trump surge in trading"""})
training_data.append({"class":"related", "sentence":"""Goldman Sachs earnings blow past expectations; shares rise"""})
training_data.append({"class":"related", "sentence":"""Goldman Sachs earnings, revenue top expectations"""})
training_data.append({"class":"related", "sentence":"""Goldman Sachs could be a big earnings winner, GE a loser, Morgan Stanley predicts"""})
training_data.append({"class":"related", "sentence":"""Goldman Sachs shares fall on 40 percent bond trading plunge despite earnings beat"""})
training_data.append({"class":"related", "sentence":"""Goldman Sachs stock sinks to 4½-month low after rare earnings miss"""})
training_data.append({"class":"related", "sentence":"""Lowe's narrows the gap with Home Depot with strong earnings beat, issues rosy outlook"""})
training_data.append({"class":"related", "sentence":"""Home Depot blows past Wall Street expectations, buoyed up by healthy housing market"""})
training_data.append({"class":"related", "sentence":"""Home Depot beats on earnings, sales; raises full-year EPS guidance"""})
training_data.append({"class":"related", "sentence":"""Home Depot nails record sales and profits, boosts full-year forecast"""})
training_data.append({"class":"related", "sentence":"""Home Depot earnings, revenue beat estimates"""})
training_data.append({"class":"related", "sentence":"""Home Depot sales beat on recovery in housing market"""})
training_data.append({"class":"related", "sentence":"""Home Depot earnings, sales top Wall Street expectations as traffic spikes"""})
training_data.append({"class":"related", "sentence":"""Home Depot same-store sales, boosted by hurricanes and fires, crush Street estimates"""})
training_data.append({"class":"related", "sentence":"""Home Depot tops Street views, raises forecast for second time this year"""})
training_data.append({"class":"related", "sentence":"""Home Depot earnings, sales top Street estimates as shoppers flock to its stores"""})
training_data.append({"class":"related", "sentence":"""IBM stock tumbles as year-over-year revenue declines for 20th consecutive quarter"""})
training_data.append({"class":"related", "sentence":"""IBM sees choppy trade after earnings beat"""})
training_data.append({"class":"related", "sentence":"""IBM tops expectations, but posts 17th quarterly revenue decline"""})
training_data.append({"class":"related", "sentence":"""IBM has long road to growth despite gains: Analyst"""})
training_data.append({"class":"related", "sentence":"""IBM tops Q4 expectations but guidance misses"""})
training_data.append({"class":"related", "sentence":"""IBM shares fall despite first growth in 23 quarters"""})
training_data.append({"class":"related", "sentence":"""For tech companies like IBM, their tax rates may go up this year under the new bill"""})
training_data.append({"class":"related", "sentence":"""Why Dow stock IBM looks undervalued into earnings"""})
training_data.append({"class":"related", "sentence":"""IBM revenue is down for the 21st quarter in a row"""})
training_data.append({"class":"related", "sentence":"""Intel shares fall 3% after missing expectations for key segment"""})
training_data.append({"class":"related", "sentence":"""Intel tops Street estimates thanks to two key segments"""})
training_data.append({"class":"related", "sentence":"""Intel falls more than 3% after earnings"""})
training_data.append({"class":"related", "sentence":"""Intel shares fall 3% after a slight miss on revenue"""})
training_data.append({"class":"related", "sentence":"""Intel shares sink on plans to cut 12,000 jobs"""})
training_data.append({"class":"related", "sentence":"""Intel earnings beat but shares fall 5%"""})
training_data.append({"class":"related", "sentence":"""Intel stock rises on earnings beat, security concerns no issue for investors"""})
training_data.append({"class":"related", "sentence":"""Intel raises guidance after earnings beat"""})
training_data.append({"class":"related", "sentence":"""Johnson & Johnson quarterly sales rise 3.9%"""})
training_data.append({"class":"related", "sentence":"""Pharma fuels Johnson & Johnson's first-quarter earnings beat"""})
training_data.append({"class":"related", "sentence":"""Johnson & Johnson's guidance impresses before 'disappointing'"""})
training_data.append({"class":"related", "sentence":"""Johnson & Johnson falls on 'disappointing' sales outlook"""})
training_data.append({"class":"related", "sentence":"""JPMorgan Chase posts stellar first quarter amid strong loan growth and trading revenue"""})
training_data.append({"class":"related", "sentence":"""Money in the bank: Booming consumer business pushes JPMorgan past Street forecasts"""})
training_data.append({"class":"related", "sentence":"""JPMorgan crushes expectations, sending shares higher"""})
training_data.append({"class":"related", "sentence":"""JPMorgan shares rise as earnings easily top estimates"""})
training_data.append({"class":"related", "sentence":"""JPMorgan shares rise on strong earnings beat"""})
training_data.append({"class":"related", "sentence":"""3 strategies to weather 'tough' earnings: JPMorgan"""})
training_data.append({"class":"related", "sentence":"""Earnings have been ‘unambiguously positive,’ and it’s going to get even better, says JPMorgan"""})
training_data.append({"class":"related", "sentence":"""JPMorgan reveals its favorite department store stocks ahead of earnings"""})
training_data.append({"class":"related", "sentence":"""JPMorgan strategist David Lebovitz: Expect a 'healthy' earnings season overall"""})
training_data.append({"class":"related", "sentence":"""JPMorgan profit tops Street estimates, but bond trading revenue plummets"""})
training_data.append({"class":"related", "sentence":"""JPMorgan smashes Wall Street estimates, but shares decline on outlook"""})
training_data.append({"class":"related", "sentence":"""McDonald's shares surge as strong restaurant sales show turnaround is working"""})
training_data.append({"class":"related", "sentence":"""McDonald's earnings, sales top Wall Street views but further improvement needed in US"""})
training_data.append({"class":"related", "sentence":"""McDonald's franchisees expect a fourth-quarter sales drop"""})
training_data.append({"class":"related", "sentence":"""McDonald's shares pop as investors cheer third-quarter beat"""})
training_data.append({"class":"related", "sentence":"""McDonald's shares down 4 percent after disappointing US sales"""})
training_data.append({"class":"related", "sentence":"""McDonald's: The key to our success is a bunch of Egg McMuffins"""})
training_data.append({"class":"related", "sentence":"""McDonald's breakfast play delivers a huge quarter"""})
training_data.append({"class":"related", "sentence":"""McDonald's shares fall on fears Dollar Menu could drag down growth"""})
training_data.append({"class":"related", "sentence":"""McDonald's same-store sales climb as promotions lure customers"""})
training_data.append({"class":"related", "sentence":"""Bet on pricier burgers pays off, sending McDonald's shares to all-time high"""})
training_data.append({"class":"related", "sentence":"""Bet on pricier burgers pays off, sending McDonald's shares to all-time high"""})
training_data.append({"class":"related", "sentence":"""Wendy's says McDonald's fresh beef tests aren't hurting its sales"""})
training_data.append({"class":"related", "sentence":"""Drugmaker Merck's profit beats estimates as margins rise"""})
training_data.append({"class":"related", "sentence":"""Merck quarterly revenue beats, raises full-year forecast"""})
training_data.append({"class":"related", "sentence":"""Merck quarterly revenue beats, raises full-year forecast"""})
training_data.append({"class":"related", "sentence":"""Merck posts better-than-expected profit, raises forecast"""})
training_data.append({"class":"related", "sentence":"""Merck revenue falls as dollar strengthens"""})
training_data.append({"class":"related", "sentence":"""Merck posts mixed fourth-quarter results as Keytruda sales skyrocket"""})
training_data.append({"class":"related", "sentence":"""Merck profit beat clouded by NotPetya attack, shares dip"""})
training_data.append({"class":"related", "sentence":"""Microsoft shares up after earnings beat"""})
training_data.append({"class":"related", "sentence":"""Microsoft stock gyrates after earnings beat"""})
training_data.append({"class":"related", "sentence":"""Microsoft dips after revenue misses expectations"""})
training_data.append({"class":"related", "sentence":"""Microsoft blows past estimates in every category, beats Street"""})
training_data.append({"class":"related", "sentence":"""Microsoft trades above 1999 all-time high after earnings beat as cloud business booms"""})
training_data.append({"class":"related", "sentence":"""Microsoft falls as much as 5% after earnings miss"""})
training_data.append({"class":"related", "sentence":"""Microsoft tops expectations, shares jump"""})
training_data.append({"class":"related", "sentence":"""Microsoft beats but stock dips, company takes $13.8 billion tax-related charge"""})
training_data.append({"class":"related", "sentence":"""Blockchain technology to boost Microsoft earnings, trader says"""})
training_data.append({"class":"related", "sentence":"""Nike's revenue misses estimates as rivals gain ground"""})
training_data.append({"class":"related", "sentence":"""Nike shares erase some of their gains as key metric spooks investors"""})
training_data.append({"class":"related", "sentence":"""Nike drops 6% as earnings beat, but sales and futures orders just miss"""})
training_data.append({"class":"related", "sentence":"""Nike shares slide 6% on mixed earnings"""})

training_data.append({"class":"related", "sentence":"""Pfizer revenue misses on lower Prevnar, Enbrel sales"""})
training_data.append({"class":"related", "sentence":"""Pfizer beats first-quarter profit estimates"""})
training_data.append({"class":"related", "sentence":"""Pfizer's profit misses as vaccine sales lag, costs rise"""})
training_data.append({"class":"related", "sentence":"""Pfizer profit just misses; company scraps cholesterol drug"""})
training_data.append({"class":"related", "sentence":"""Pfizer beats estimates but maintains 2016 profit forecast"""})
training_data.append({"class":"related", "sentence":"""Pfizer earnings, revenue top expectations"""})
training_data.append({"class":"related", "sentence":"""Pfizer profit tops estimates as it booked an $11 billion tax gain"""})
training_data.append({"class":"related", "sentence":"""Pfizer beats profit estimates and raises 2017 earnings forecast"""})
training_data.append({"class":"related", "sentence":"""How were P&G;'s earnings? It depends who you ask, with results providing fodder for both sides"""})
training_data.append({"class":"related", "sentence":"""P&G; tops Wall Street views, but activist Peltz says it must fix 'root cause' of its slow growth"""})
training_data.append({"class":"related", "sentence":"""P&G; tops Wall Street views, but activist Peltz says it must fix 'root cause' of its slow growth"""})
training_data.append({"class":"related", "sentence":"""P&G; profit and sales beat Wall Street estimates, raises guidance"""})
training_data.append({"class":"related", "sentence":"""P&G; profit beats on cost cuts, demand for home care goods"""})
training_data.append({"class":"related", "sentence":"""After 'lost decade', P&G; is a buy here as profit growth returns: Deutsche Bank"""})
training_data.append({"class":"related", "sentence":"""P&G; tops Wall Street estimates, helped by continued cost-cutting"""})
training_data.append({"class":"related", "sentence":"""P&G; reports better-than-expected rise in profit, but quarterly sales drop 7%"""})
training_data.append({"class":"related", "sentence":"""We'll fight Dollar Shave Club over patent: P&G;"""})
training_data.append({"class":"related", "sentence":"""P&G; regains sales momentum, but pricing is still an issue"""})
training_data.append({"class":"related", "sentence":"""Procter & Gamble sales disappoint on geopolitical challenges"""})
training_data.append({"class":"related", "sentence":"""Travelers profit falls on higher catastrophe losses"""})
training_data.append({"class":"related", "sentence":"""Insurer Travelers profit slumps on significant catastrophe losses"""})
training_data.append({"class":"related", "sentence":"""Travelers quarterly profit falls on higher catastrophe losses"""})
training_data.append({"class":"related", "sentence":"""Insurer Travelers reports 22.8% drop in profit"""})
training_data.append({"class":"related", "sentence":"""Texas storms hit insurer Travelers profit"""})
training_data.append({"class":"related", "sentence":"""Insurer Travelers profit falls 16.6%"""})
training_data.append({"class":"related", "sentence":"""Insurer Travelers profit beats as investment earnings rise"""})
training_data.append({"class":"related", "sentence":"""United Technologies earnings and revenue top analysts' expectations"""})
training_data.append({"class":"related", "sentence":"""United Technologies quarterly profit rises 17.8%"""})
training_data.append({"class":"related", "sentence":"""United Technologies beats estimates, lifts low end of full-year guidance"""})
training_data.append({"class":"related", "sentence":"""UnitedHealth profit beats estimates on Optum unit strength"""})
training_data.append({"class":"related", "sentence":"""Health insurer UnitedHealth reports higher profit"""})
training_data.append({"class":"related", "sentence":"""Health insurer UnitedHealth's revenue rises 30%"""})
training_data.append({"class":"related", "sentence":"""UnitedHealth stock jumps after insurer's profit more than doubles on a one-time tax gain"""})
training_data.append({"class":"related", "sentence":"""UnitedHealth shares dip on disappointing earnings forecast for 2018"""})
training_data.append({"class":"related", "sentence":"""UnitedHealth tops profit estimates on strength in Optum business"""})
training_data.append({"class":"related", "sentence":"""Insurer UnitedHealth's quarterly profit jumps 30%"""})
training_data.append({"class":"related", "sentence":"""UnitedHealth earnings top expectations; memberships increase"""})
training_data.append({"class":"related", "sentence":"""What to watch in UnitedHealth’s earnings"""})
training_data.append({"class":"related", "sentence":"""CFO: Why J&J;'s three units are best as one company"""})
training_data.append({"class":"related", "sentence":"""J&J; sales fall on strong dollar"""})
training_data.append({"class":"related", "sentence":"""New cancer drugs help J&J; top profit estimates"""})
training_data.append({"class":"related", "sentence":"""J&J; raises 2017 forecast as earnings beats the Street"""})
training_data.append({"class":"related", "sentence":"""J&J; Q4 sales up 1.7 pct, plans to divest diabetes care division"""})
training_data.append({"class":"related", "sentence":"""Verizon beats on earnings, but revenue falls short of estimates"""})
training_data.append({"class":"related", "sentence":"""As earnings beat, Yahoo says it's still preparing to merge with Verizon"""})
training_data.append({"class":"related", "sentence":"""Verizon beats earnings estimates but misses on revenue"""})
training_data.append({"class":"related", "sentence":"""Verizon matches expectations, but revenue is light"""})
training_data.append({"class":"related", "sentence":"""Verizon shares tick higher after mixed quarterly results"""})
training_data.append({"class":"related", "sentence":"""Verizon will launch over-the-top service before year-end with NFL as key piece, analyst predicts"""})
training_data.append({"class":"related", "sentence":"""Verizon added more phone customers than Wall Street expected last quarter, boosting sales"""})
training_data.append({"class":"related", "sentence":"""A buried clue in Verizon earnings: Wearables are gaining steam"""})
training_data.append({"class":"related", "sentence":"""Verizon matches earnings, beats revenue expectations in first full quarter with unlimited data plans"""})
training_data.append({"class":"related", "sentence":"""Verizon earnings, revenue miss Street estimates as wireless subscribers drop"""})
training_data.append({"class":"related", "sentence":"""Verizon shares fall after quarterly earnings come in below Street's expectations"""})
training_data.append({"class":"related", "sentence":"""Yahoo delays closing of Verizon deal, beats on earnings"""})
training_data.append({"class":"related", "sentence":"""T-Mobile trolls Verizon for releasing its earnings report on 4/20"""})
training_data.append({"class":"related", "sentence":"""Visa profit, revenue beat analysts' estimates"""})
training_data.append({"class":"related", "sentence":"""Visa shares pop 2% on earnings beat"""})
training_data.append({"class":"related", "sentence":"""Visa's profit beats Street view on healthy payment volumes"""})
training_data.append({"class":"related", "sentence":"""European expansion, payments growth help Visa beat earning expectations"""})
training_data.append({"class":"related", "sentence":"""Visa gains 3% after earnings beat, company announces $5 billion buyback"""})
training_data.append({"class":"related", "sentence":"""Wal-Mart's US stores just had their best quarter in more than four years"""})
training_data.append({"class":"related", "sentence":"""Wal-Mart beats on earnings, raises lower end of guidance, but revenue falls short"""})
training_data.append({"class":"related", "sentence":"""This chart explains Wal-Mart's big win over Target"""})
training_data.append({"class":"related", "sentence":"""Wal-Mart just rang up its biggest same-store sales gain in 4 years"""})
training_data.append({"class":"related", "sentence":"""Analyst: Why Wal-Mart can make a comeback"""})
training_data.append({"class":"related", "sentence":"""Wal-Mart surges to all-time high after earnings crush expectations"""})
training_data.append({"class":"related", "sentence":"""Wal-Mart beats on earnings, same-store sales climb as online purchases grow 60%"""})
training_data.append({"class":"related", "sentence":"""Wal-Mart earnings top Street estimates as retailer's digital sales jump 63%"""})
training_data.append({"class":"related", "sentence":"""Walmart's e-commerce growth wanes, sending shares tumbling"""})
training_data.append({"class":"related", "sentence":"""Campbell Soup organic sales fall as dispute with Walmart continues"""})
training_data.append({"class":"related", "sentence":"""ExxonMobil earnings badly miss expectations as profits sink 59%"""})
training_data.append({"class":"related", "sentence":"""United Tech's quarterly profit slumps 8 percent"""})
training_data.append({"class":"related", "sentence":"""United Tech quarterly revenue rises 2.7%"""})
training_data.append({"class":"related", "sentence":"""United Tech stands by 2017 forecast on demand for jet engines"""})
training_data.append({"class":"related", "sentence":"""United Tech's quarterly revenue rises 1.25%"""})



training_data.append({"class":"non-related", "sentence":"""Buyout firm Blackstone Q3 earnings beat estimates"""})
training_data.append({"class":"non-related", "sentence":"""Tesla shares soar after posting second quarterly profit ever"""})
training_data.append({"class":"non-related", "sentence":"""Deutsche Bank posts surprise profit and hikes legal provision; 'working hard' on DOJ issue"""})
training_data.append({"class":"non-related", "sentence":"""Statoil cuts capital expenditure again after posting third-quarter miss"""})
training_data.append({"class":"non-related", "sentence":"""VW raises full-year revenue guidance after third-quarter sales increase"""})
training_data.append({"class":"non-related", "sentence":"""Barclays beats estimates for third quarter with bond-trading boost"""})
training_data.append({"class":"non-related", "sentence":"""Samsung co-chief Shin issues apology as Q3 profit slumps 30% after Note 7 debacle"""})
training_data.append({"class":"non-related", "sentence":"""Traders expect to see $53 billion in earnings moves from two tech giants"""})
training_data.append({"class":"non-related", "sentence":"""NCR surges 14% after earnings and revenue top expectations"""})
training_data.append({"class":"non-related", "sentence":"""Edwards Lifesciences plunge after third-quarter sales disappoint"""})
training_data.append({"class":"non-related", "sentence":"""Alibaba is surging into earnings — here’s how to play it: Trader"""})
training_data.append({"class":"non-related", "sentence":"""Goldman’s plan for making money on earnings"""})
training_data.append({"class":"non-related", "sentence":"""Buy cloud play ServiceNow before earnings on accelerating growth, UBS says"""})
training_data.append({"class":"non-related", "sentence":"""Comcast quarterly earnings, revenue top analysts' expectations"""})
training_data.append({"class":"non-related", "sentence":"""Oreo maker Mondelez's quarterly profit tops estimates"""})
training_data.append({"class":"non-related", "sentence":"""Southwest Airlines shares plunge after quarterly profit falls 33.6 percent"""})
training_data.append({"class":"non-related", "sentence":"""Heineken hikes beer sales but sees bigger currency hit"""})
training_data.append({"class":"non-related", "sentence":"""Chipotle turnaround still slower than expected"""})
training_data.append({"class":"non-related", "sentence":"""Panera shrugs off industry slump, topping estimates and raising forecast"""})
training_data.append({"class":"non-related", "sentence":"""Crane shares soar after earnings beat"""})
training_data.append({"class":"non-related", "sentence":"""Masco shares drag homebuilders after earnings miss"""})
training_data.append({"class":"non-related", "sentence":"""Shares of Baker Hughes jump on smaller-than-expected loss"""})
training_data.append({"class":"non-related", "sentence":"""Sherwin-Williams shares sink after earnings miss"""})
training_data.append({"class":"non-related", "sentence":"""Whirlpool shares plunge after earnings miss, tracking for worst day in nearly 5 years"""})
training_data.append({"class":"non-related", "sentence":"""Nielsen Holdings shares plummet after earnings disappoint"""})
training_data.append({"class":"non-related", "sentence":"""Under Armour shares plunge after posting slowest sales growth in six years"""})
training_data.append({"class":"non-related", "sentence":"""Lilly third-quarter results miss estimates"""})
training_data.append({"class":"non-related", "sentence":"""JetBlue profit misses as costs rise"""})
training_data.append({"class":"non-related", "sentence":"""Lockheed Martin's revenue rises 14.8 percent"""})
training_data.append({"class":"non-related", "sentence":"""General Motors third-quarter earnings widely beat expectations"""})
training_data.append({"class":"non-related", "sentence":"""Burger King/Tim Hortons owner's profit beats on new menu items"""})
training_data.append({"class":"non-related", "sentence":"""GE profit up but revenue forecast trimmed amid sluggish economy"""})
training_data.append({"class":"non-related", "sentence":"""Honeywell beats analysts' estimates on earnings and revenue"""})
training_data.append({"class":"non-related", "sentence":"""Paypal shares rally after revenue tops expectations"""})
training_data.append({"class":"non-related", "sentence":"""Earnings will drive market, and they're expected to grow 13% to 14% next year, expert says"""})
training_data.append({"class":"non-related", "sentence":"""Dunkin' Brands revenue misses on fewer restaurant openings"""})
training_data.append({"class":"non-related", "sentence":"""Walgreens profit jumps, Rite Aid deal seen closing in 2017"""})
training_data.append({"class":"non-related", "sentence":"""Mattel sales beat estimates as Barbie shines"""})
training_data.append({"class":"non-related", "sentence":"""Ebay's holiday-quarter forecast disappoints; shares slump"""})
training_data.append({"class":"non-related", "sentence":"""Halliburton posts surprise profit as expenses fall"""})
training_data.append({"class":"non-related", "sentence":"""Morgan Stanley roars to big quarter on trading surge; shares higher"""})
training_data.append({"class":"non-related", "sentence":"""BlackRock reports earnings that beat expectations, revenue misses"""})
training_data.append({"class":"non-related", "sentence":"""Domino's shares pop on earnings beat, strong quarterly sales"""})
training_data.append({"class":"non-related", "sentence":"""Bank of America crushes earnings on trading surge; shares rise"""})
training_data.append({"class":"non-related", "sentence":"""Netflix sees best day since 2013"""})
training_data.append({"class":"non-related", "sentence":"""Citigroup tops Wall Street expectations for earnings and revenue"""})
training_data.append({"class":"non-related", "sentence":"""Scandal-plagued Wells Fargo reports results that edge out forecasts"""})
training_data.append({"class":"non-related", "sentence":"""Good news for travelers — Delta CEO says airfares haven't bottomed yet"""})
training_data.append({"class":"non-related", "sentence":"""Alcoa sinks after earnings, revenue fall short of expectations"""})
training_data.append({"class":"non-related", "sentence":"""Monsanto surprises with adjusted profit as expenses drop"""})
training_data.append({"class":"non-related", "sentence":"""Micron Technology's first-quarter guidance weighs on shares"""})
training_data.append({"class":"non-related", "sentence":"""Darden Restaurants shares climb on raised outlook and new buyback plan"""})
training_data.append({"class":"non-related", "sentence":"""General Mills sales fall for fifth straight quarter"""})
training_data.append({"class":"non-related", "sentence":"""FedEx earnings beat estimates"""})
training_data.append({"class":"non-related", "sentence":"""Ascena shares plunge after earnings miss, weaker-than-expected guidance"""})
training_data.append({"class":"non-related", "sentence":"""Homebuilders tumble on weak housing data, Lennar outlook"""})
training_data.append({"class":"non-related", "sentence":"""Homebuilder Lennar's profit, revenue tops estimates; orders rise"""})
training_data.append({"class":"non-related", "sentence":"""Oracle's profit forecast misses estimates; shares slip"""})
training_data.append({"class":"non-related", "sentence":"""US elections weigh on Barnes & Noble same-store sales forecast"""})
training_data.append({"class":"non-related", "sentence":"""Lululemon same-store sales fall short, sending shares lower"""})
training_data.append({"class":"non-related", "sentence":"""VeriFone shares on track for worst day in 3 months after giving dismal guidance"""})
training_data.append({"class":"non-related", "sentence":"""Campbell Soup reports 'disappointing' fresh, organic foods sales"""})
training_data.append({"class":"non-related", "sentence":"""Cloud management company Box's quarterly revenue jumps 30%"""})
training_data.append({"class":"non-related", "sentence":"""H&R; Block stock tumbles on earnings miss"""})
training_data.append({"class":"non-related", "sentence":"""Chico's shares pop after earnings beat"""})
training_data.append({"class":"non-related", "sentence":"""Shares of Veeva Systems fly after beating earnings expectations"""})
training_data.append({"class":"non-related", "sentence":"""Palo Alto forecasts revenue below estimates, shares drop"""})
training_data.append({"class":"non-related", "sentence":"""Fashion retailer shares nosedive after earnings"""})
training_data.append({"class":"non-related", "sentence":"""Ulta shares stumble on slightly disappointing earnings guidance"""})
training_data.append({"class":"non-related", "sentence":"""Banks just soared to most profitable quarter EVER"""})
training_data.append({"class":"non-related", "sentence":"""Workday shares spike after subscription sales rise"""})
training_data.append({"class":"non-related", "sentence":"""Tiffany's profit unexpectedly rises on lower costs, higher prices"""})
training_data.append({"class":"non-related", "sentence":"""Food stamp cuts, lower food prices weigh on dollar stores"""})
training_data.append({"class":"non-related", "sentence":"""Sears posts quarterly loss, taking debt from CEO's hedge fund"""})
training_data.append({"class":"non-related", "sentence":"""HP beats estimates, weak printer demand weighs on forecast"""})
training_data.append({"class":"non-related", "sentence":"""Express shares plummet after disappointing sales from weak store traffic"""})
training_data.append({"class":"non-related", "sentence":"""Intuit stock falls after weak first quarter guidance"""})
training_data.append({"class":"non-related", "sentence":"""Analysts expect little luster from jewelers earnings"""})
training_data.append({"class":"non-related", "sentence":"""Best Buy shares soar 15% on surprise rise in same-store sales"""})
training_data.append({"class":"non-related", "sentence":"""Toll Brothers shares gain 9%, on track for best day since Oct 2011"""})
training_data.append({"class":"non-related", "sentence":"""Deere shares jump 13%, plows past Street, boosts forecast"""})
training_data.append({"class":"non-related", "sentence":"""Estee Lauder shares slide after sales, guidance miss"""})
training_data.append({"class":"non-related", "sentence":"""Stephen Curry, Kevin Durant help lift Foot Locker's sales"""})
training_data.append({"class":"non-related", "sentence":"""Deere posts lower quarterly profit, raises full-year outlook"""})
training_data.append({"class":"non-related", "sentence":"""NetApp shares surge after easily topping earnings expectations"""})
training_data.append({"class":"non-related", "sentence":"""Shares of 58.com plummet 14% after the company gives disappointing guidance"""})
training_data.append({"class":"non-related", "sentence":"""Victoria's Secret owner's shares jump after surprising investors on earnings"""})
training_data.append({"class":"non-related", "sentence":"""Target beats on earnings, lowers full-year guidance"""})
training_data.append({"class":"non-related", "sentence":"""Lowe's shares sink as earnings, revenue miss, full-year guidance cut"""})
training_data.append({"class":"non-related", "sentence":"""Staples forecasts 15th consecutive quarterly sales decline"""})
training_data.append({"class":"non-related", "sentence":"""Popeyes shares plunge on downbeat outlook, cites industrywide weakness"""})
training_data.append({"class":"non-related", "sentence":"""Tencent beats estimates with smartphone gaming boost"""})
training_data.append({"class":"non-related", "sentence":"""Dick's shares jump 8 percent after chain tops estimates, raises guidance"""})
training_data.append({"class":"non-related", "sentence":"""Hain Celestial plunges after it says accounting snafu will delay results"""})
training_data.append({"class":"non-related", "sentence":"""Concordia shares plunge 27% on slashed outlook, suspended dividend"""})
training_data.append({"class":"non-related", "sentence":"""Ruby Tuesday shares plummet 12% on disappointing sales, restaurant closures"""})
training_data.append({"class":"non-related", "sentence":"""JC Penney posts smaller-than-expected loss, but revenues fall short"""})
training_data.append({"class":"non-related", "sentence":"""Macy's soars 16% after topping Street estimates, unveiling plans to close 100 stores"""})
training_data.append({"class":"non-related", "sentence":"""Three stocks to buy on Macy's big earnings beat"""})
training_data.append({"class":"non-related", "sentence":"""Olympic sized scandals"""})
training_data.append({"class":"non-related", "sentence":"""Kohl's quarterly sales beat estimates"""})
training_data.append({"class":"non-related", "sentence":"""Alibaba is 'just killing it' on mobile, says Vice Chairman Joe Tsai"""})
training_data.append({"class":"non-related", "sentence":"""Shake Shack gets grilled, shares down 9 pct after earnings"""})
training_data.append({"class":"non-related", "sentence":"""Why this summer's rally will look 'silly' in hindsight"""})
training_data.append({"class":"non-related", "sentence":"""A set of loser stocks has turned it around, and Wall Street is now the winner"""})
training_data.append({"class":"non-related", "sentence":"""Wendy's stock falls nearly 3 percent as investors fret weakening sales trends"""})
training_data.append({"class":"non-related", "sentence":"""Disney tops estimates, announces stake in part of MLB's digital unit"""})
training_data.append({"class":"non-related", "sentence":"""Gap shares drop 6% as June's turnaround evaporates"""})
training_data.append({"class":"non-related", "sentence":"""Endo International shares surge after second-quarter earnings top estimates"""})
training_data.append({"class":"non-related", "sentence":"""American Air higher, United Continental off after traffic numbers"""})
training_data.append({"class":"non-related", "sentence":"""Disney reports today. Here's what What Wall Street is worried about"""})
training_data.append({"class":"non-related", "sentence":"""Earnings lift European shares; DAX jumps 2.5%"""})
training_data.append({"class":"non-related", "sentence":"""Valeant maintains full-year forecast, shares surge 18%"""})
training_data.append({"class":"non-related", "sentence":"""Rupert Murdoch's News Corp posts mixed second-quarter earnings"""})
training_data.append({"class":"non-related", "sentence":"""LendingClub stock recovers after wider loss than expected, CFO steps down"""})
training_data.append({"class":"non-related", "sentence":"""Allergan falls 3% after revenue disappoints, as Alzheimer drug loses exclusivity"""})
training_data.append({"class":"non-related", "sentence":"""Tyson Foods rally after posting strong sales across all categories"""})
training_data.append({"class":"non-related", "sentence":"""Sotheby's surges as quarterly results top expectations"""})
training_data.append({"class":"non-related", "sentence":"""Berkshire profit up 25% as insurance helps, BNSF weighs"""})
training_data.append({"class":"non-related", "sentence":"""Shares of Nu Skin freshen up after earnings beat and raised guidance"""})
training_data.append({"class":"non-related", "sentence":"""Lions Gate stock roars after revenue beat, assisted by 'Now You See Me 2'"""})
training_data.append({"class":"non-related", "sentence":"""Activision Blizzard beats earnings as competitive gaming gains ground"""})
training_data.append({"class":"non-related", "sentence":"""Kraft Heinz shares pop 4.5% on increased quarterly dividends, earnings beat"""})
training_data.append({"class":"non-related", "sentence":"""LinkedIn beats the Street as sales soar 31%"""})
training_data.append({"class":"non-related", "sentence":"""MetLife plunges 8.5% after earnings, $2 billion charge"""})
training_data.append({"class":"non-related", "sentence":"""Toyota expects SUVs to drive sales"""})
training_data.append({"class":"non-related", "sentence":"""Square stock bounces 13% on narrower-than-expected loss"""})
training_data.append({"class":"non-related", "sentence":"""Party City shares surge after earnings surprise to the upside"""})
training_data.append({"class":"non-related", "sentence":"""Chesapeake Energy drops after earnings miss, asset sale plan"""})
training_data.append({"class":"non-related", "sentence":"""Viacom stock rises after surprise beat on earnings and revenues"""})
training_data.append({"class":"non-related", "sentence":"""Corn Flakes maker Kellogg's sales miss analysts' estimates"""})
training_data.append({"class":"non-related", "sentence":"""Burger King owner sales fall short despite Chicken Rings, Mac 'N Cheetos boost"""})
training_data.append({"class":"non-related", "sentence":"""Time Inc's quarterly revenue misses estimates"""})
training_data.append({"class":"non-related", "sentence":"""Adidas sees recovery at golf business it hopes to sell"""})
training_data.append({"class":"non-related", "sentence":"""Tesla misses Wall Street targets, but logs gains in vehicle production"""})
training_data.append({"class":"non-related", "sentence":"""Jack in the Box shares pop 7 pct on earnings beat"""})
training_data.append({"class":"non-related", "sentence":"""Papa John's boosts 2016 forecast, sending shares up 5 percent"""})
training_data.append({"class":"non-related", "sentence":"""AIG pops on earnings and a $3 billion buyback increase"""})
training_data.append({"class":"non-related", "sentence":"""The ‘Trump effect’: S&P; companies talk candidate on earnings calls"""})
training_data.append({"class":"non-related", "sentence":"""Vroom! Avis shares jump after topping revenue estimate"""})
training_data.append({"class":"non-related", "sentence":"""Kate Spade shares plunge 20 percent as growth abruptly slows"""})
training_data.append({"class":"non-related", "sentence":"""Time Warner beats on second-quarter earnings, misses on revenue"""})
training_data.append({"class":"non-related", "sentence":"""Crocs dives after disappointing second-quarter earnings, lower guidance"""})
training_data.append({"class":"non-related", "sentence":"""Clorox misses 4Q profit forecasts"""})
training_data.append({"class":"non-related", "sentence":"""HSBC's profit drops almost 29%; warns on Panama Papers"""})
training_data.append({"class":"non-related", "sentence":"""Royal Caribbean shares sink after Q2 results; CEO sees no immediate Zika effect"""})
training_data.append({"class":"non-related", "sentence":"""Mallinckrodt leads S&P; after second-quarter results beat the Street"""})
training_data.append({"class":"non-related", "sentence":"""Kate Spade shares plunge after slashing its full-year sales forecast"""})
training_data.append({"class":"non-related", "sentence":"""Avon Products climbs higher after profits beat Street expectations"""})
training_data.append({"class":"non-related", "sentence":"""SodaStream beats revenue estimates"""})
training_data.append({"class":"non-related", "sentence":"""Steven Madden earnings match estimates"""})
training_data.append({"class":"non-related", "sentence":"""AMC's disappointing quarter was an 'anomaly,' CEO says"""})
training_data.append({"class":"non-related", "sentence":"""Expedia shares drop after missing revenue estimates"""})
training_data.append({"class":"non-related", "sentence":"""Newell Brands stock jumps after beating earnings"""})
training_data.append({"class":"non-related", "sentence":"""UPS earnings in line and revenues beat in Q2; led by international growth"""})
training_data.append({"class":"non-related", "sentence":"""Drugmaker AbbVie bumps up profit forecast on strong Humira sales"""})
training_data.append({"class":"non-related", "sentence":"""Spirit Airlines second-quarter earnings top expectations"""})
training_data.append({"class":"non-related", "sentence":"""Amazon shares rise after earnings crush forecasts"""})
training_data.append({"class":"non-related", "sentence":"""Google parent Alphabet gains after earnings beat"""})
training_data.append({"class":"non-related", "sentence":"""GNC shares plunge after CEO resigns and company suspends earnings guidance"""})
training_data.append({"class":"non-related", "sentence":"""Top investor Navellier, known for earnings bets, likes this chipmaker"""})
training_data.append({"class":"non-related", "sentence":"""Ford steers toward its worst day in 5 years after disappointing earnings"""})
training_data.append({"class":"non-related", "sentence":"""Cirrus Logic soars after earnings beat and strong guidance"""})
training_data.append({"class":"non-related", "sentence":"""We're at the halfway mark for earnings. Here's the good news..."""})
training_data.append({"class":"non-related", "sentence":"""The last of the FANG earnings could spark a $50 billion shift in market cap"""})
training_data.append({"class":"non-related", "sentence":"""MasterCard reports 6.7% rise in profit"""})
training_data.append({"class":"non-related", "sentence":"""Lackluster US, China sales drag on Ford Motor profit; shares drop"""})
training_data.append({"class":"non-related", "sentence":"""Infinera shares shed a third of their value after dismal sales forecast"""})
training_data.append({"class":"non-related", "sentence":"""New York Times reports another loss as ad sales decline"""})
training_data.append({"class":"non-related", "sentence":"""Colgate-Palmolive beats by a penny; sales decline forecast"""})
training_data.append({"class":"non-related", "sentence":"""ConocoPhillips reduces 2016 capex, aims to return more cash to shareholders"""})
training_data.append({"class":"non-related", "sentence":"""Hershey's profit beats, net sales rise for 1st time this year"""})
training_data.append({"class":"non-related", "sentence":"""Sales of flagship drug Revlimid drive Celgene profit; forecast raised"""})
training_data.append({"class":"non-related", "sentence":"""Harley-Davidson second-quarter income drops on soft US sales"""})
training_data.append({"class":"non-related", "sentence":"""Facebook's exploding ad revenue sends earnings soaring past estimates"""})
training_data.append({"class":"non-related", "sentence":"""Facebook's over-the-top quarterly report owes a lot to the phone in your pocket"""})
training_data.append({"class":"non-related", "sentence":"""Shell sees quarterly profits plummet 70% as low oil price bites"""})
training_data.append({"class":"non-related", "sentence":"""Whole Foods stock sinks after key metric disappoints Street"""})
training_data.append({"class":"non-related", "sentence":"""GoPro tops estimates"""})
training_data.append({"class":"non-related", "sentence":"""BNP Paribas struggles for growth in low interest rate environment"""})
training_data.append({"class":"non-related", "sentence":"""Comcast beats on earnings and revenue"""})
training_data.append({"class":"non-related", "sentence":"""Fiat Chrysler raises 2016 forecast despite recall profit hit"""})
training_data.append({"class":"non-related", "sentence":"""Oreo maker Mondelez's revenue falls for 11th straight quarter"""})
training_data.append({"class":"non-related", "sentence":"""Hardwood flooring maker Lumber Liquidators sales fall"""})
training_data.append({"class":"non-related", "sentence":"""Bayer drugs secure earnings beat, offset weak crop chems"""})
training_data.append({"class":"non-related", "sentence":"""Twitter shares drop 10% after guidance disappoints"""})
training_data.append({"class":"non-related", "sentence":"""Lilly sales beat estimates on demand for new drugs"""})
training_data.append({"class":"non-related", "sentence":"""Twitter's user numbers, slowing revenue growth in focus in Q2 earnings"""})
training_data.append({"class":"non-related", "sentence":"""Gilead cuts 2016 sales forecast, cites hepatitis C drugs"""})
training_data.append({"class":"non-related", "sentence":"""Sprint's revenue beats estimates as it adds subscribers"""})
training_data.append({"class":"non-related", "sentence":"""GE profit beats estimates as power business revenue rises"""})
training_data.append({"class":"non-related", "sentence":"""American Airlines profit beats estimates as costs fall"""})
training_data.append({"class":"non-related", "sentence":"""Starbucks shares drop after same-store sales around the world miss estimates"""})
training_data.append({"class":"non-related", "sentence":"""Chipotle loyalty program offers investors something to chew on"""})
training_data.append({"class":"non-related", "sentence":"""Dunkin' Brands shares fall on soft revenue, international headwinds"""})
training_data.append({"class":"non-related", "sentence":"""GM raises full-year forecast after strong second-quarter result"""})
training_data.append({"class":"non-related", "sentence":"""Southwest Airlines reports record quarterly profit, but misses estimates"""})
training_data.append({"class":"non-related", "sentence":"""Blackstone earnings beat forecasts on real estate, energy"""})
training_data.append({"class":"non-related", "sentence":"""Morgan Stanley solidly beats earnings expectations"""})
training_data.append({"class":"non-related", "sentence":"""Banks' earnings stay on a roll as Goldman tops the Street"""})
training_data.append({"class":"non-related", "sentence":"""Yahoo CEO offers results no one cares about and no news on sale that everyone does"""})
training_data.append({"class":"non-related", "sentence":"""As uncertainty drags on, Mayer says she's committed to Yahoo"""})
training_data.append({"class":"non-related", "sentence":"""Netflix drops 15% as subscriber numbers disappoint"""})
training_data.append({"class":"non-related", "sentence":"""Bank of America earnings top expectations"""})
training_data.append({"class":"non-related", "sentence":"""Hasbro stock falls 7 percent amid concerns about sales of boys' toys"""})
training_data.append({"class":"non-related", "sentence":"""As it nears sale, Yahoo's earnings likely to reveal continued decline"""})
training_data.append({"class":"non-related", "sentence":"""Citigroup earnings handily top Wall Street expectations"""})
training_data.append({"class":"non-related", "sentence":"""Wells Fargo second-quarter earnings match estimates"""})
training_data.append({"class":"non-related", "sentence":"""BlackRock posts second-quarter profits that meet estimates"""})
training_data.append({"class":"non-related", "sentence":"""Yum Brands shares rise after earnings beat"""})
training_data.append({"class":"non-related", "sentence":"""CSX shares rise 4 pct as surprise Q2 results beat expectations"""})
training_data.append({"class":"non-related", "sentence":"""Seagate's fourth-quarter revenue estimate beats Street view"""})
training_data.append({"class":"non-related", "sentence":"""Alcoa tops analyst estimates, stock jumps 4 percent"""})
training_data.append({"class":"non-related", "sentence":"""Drugstore operator Walgreens quarterly sales rise 2.4%"""})
training_data.append({"class":"non-related", "sentence":"""Pier 1 shares drop 6% on bigger than expected loss"""})
training_data.append({"class":"non-related", "sentence":"""Pensions hit FedEx, may weigh on fiscal 2017 results"""})
training_data.append({"class":"non-related", "sentence":"""CarMax stock dips after weak quarterly report"""})
training_data.append({"class":"non-related", "sentence":"""Canadian Pacific shares slide amid weak guidance"""})
training_data.append({"class":"non-related", "sentence":"""United Continental shares rally amid brighter revenue forecast"""})
training_data.append({"class":"non-related", "sentence":"""Oracle shares rise as sales beat estimates"""})
training_data.append({"class":"non-related", "sentence":"""Rite Aid shares slip as first-quarter earnings fall short"""})
training_data.append({"class":"non-related", "sentence":"""Supermarket operator Kroger's quarterly profit up about 10%"""})
training_data.append({"class":"non-related", "sentence":"""H&R; Block pops 7% on earnings beat"""})
training_data.append({"class":"non-related", "sentence":"""Valeant shares crater after profit misses estimates, company cuts forecast"""})
training_data.append({"class":"non-related", "sentence":"""Citigroup CEO points to 25 percent drop in quarterly results"""})
training_data.append({"class":"non-related", "sentence":"""This is what’s really driving Costco’s stock, Jim Cramer says"""})
training_data.append({"class":"non-related", "sentence":"""Lions Gate shares pop after posting a surprise profit"""})
training_data.append({"class":"non-related", "sentence":"""PVH shares advance as Calvin Klein, Tommy Hilfiger drive Q1 beat"""})
training_data.append({"class":"non-related", "sentence":"""Dollar stores boosted after beating Street"""})
training_data.append({"class":"non-related", "sentence":"""Sears posts bigger loss, explores options for two businesses"""})
training_data.append({"class":"non-related", "sentence":"""Gap reports earnings in line with expectations, announces 75 store closings"""})
training_data.append({"class":"non-related", "sentence":"""L Brands trims full-year guidance as sales fall short"""})
training_data.append({"class":"non-related", "sentence":"""Target earnings top expectations, but revenue is light"""})
training_data.append({"class":"non-related", "sentence":"""Staples earnings beat analysts' expectations by a penny a share"""})
training_data.append({"class":"non-related", "sentence":"""Lowe's earnings, revenue beat analysts' expectations"""})
training_data.append({"class":"non-related", "sentence":"""Perrigo shares sway on quarterly results"""})
training_data.append({"class":"non-related", "sentence":"""Agilent shares up after earnings beat"""})
training_data.append({"class":"non-related", "sentence":"""TJX stock gains after retailer beats earnings estimates"""})
training_data.append({"class":"non-related", "sentence":"""Red Robin shares stumble after sales miss"""})
training_data.append({"class":"non-related", "sentence":"""Children’s Place bounces on boosted forecast"""})
training_data.append({"class":"non-related", "sentence":"""JC Penney shares fall after posting mixed results"""})
training_data.append({"class":"non-related", "sentence":"""Shake Shack results beat estimates, raises forecast"""})
training_data.append({"class":"non-related", "sentence":"""Macy's profit beats, but the retailer cut its full-year outlook"""})
training_data.append({"class":"non-related", "sentence":"""Wendy's shares fall despite earnings beat, raised guidance"""})
training_data.append({"class":"non-related", "sentence":"""Disney shares drop 6 percent as earnings, sales miss"""})
training_data.append({"class":"non-related", "sentence":"""Lumber Liquidators sales sink 10.2% amid struggle to reassure customers"""})
training_data.append({"class":"non-related", "sentence":"""Yelp shares pop 8 pct as earnings beat"""})
training_data.append({"class":"non-related", "sentence":"""GoPro shares swing after results; sales fall 50%"""})
training_data.append({"class":"non-related", "sentence":"""Square's shares drop 13% on quarterly loss"""})
training_data.append({"class":"non-related", "sentence":"""Time Inc. revenue rises as digital acquisitions pay"""})
training_data.append({"class":"non-related", "sentence":"""SeaWorld reports Q1 loss"""})
training_data.append({"class":"non-related", "sentence":"""Alibaba's revenue rises 39% as more shoppers buy online"""})
training_data.append({"class":"non-related", "sentence":"""Tesla pops 4% on results, production outlook"""})
training_data.append({"class":"non-related", "sentence":"""Whole Foods Market up after it beats on earnings per share, misses on revenue"""})
training_data.append({"class":"non-related", "sentence":"""Time Warner revenue boosted by Turner, HBO"""})
training_data.append({"class":"non-related", "sentence":"""Kate Spade sales gets boost from North America demand"""})
training_data.append({"class":"non-related", "sentence":"""Shell profit tumbles as lower crude price hurts"""})
training_data.append({"class":"non-related", "sentence":"""AB InBev suffers weak start to year after Brazil slump"""})
training_data.append({"class":"non-related", "sentence":"""Weak quarter weighs on AIG shares"""})
training_data.append({"class":"non-related", "sentence":"""Jim Cramer: Here's why Clorox had a 'fabulous quarter'"""})
training_data.append({"class":"non-related", "sentence":"""Sprint forecasts jump in full-year operating income"""})
training_data.append({"class":"non-related", "sentence":"""UBS hit by 'double whammy' of low interest rates and regulations"""})
training_data.append({"class":"non-related", "sentence":"""Here's what earnings season has taught us about where tech is headed"""})
training_data.append({"class":"non-related", "sentence":"""AIG earnings per share drop 47%, shares dip 3%"""})
training_data.append({"class":"non-related", "sentence":"""Exxon doesn't look like an oil company anymore, analyst says"""})
training_data.append({"class":"non-related", "sentence":"""Amazon blows past earnings estimates, shares pop 12%"""})
training_data.append({"class":"non-related", "sentence":"""LinkedIn shares soar after big beat on top and bottom"""})
training_data.append({"class":"non-related", "sentence":"""Traders: Beware these earnings sucker's rallies"""})
training_data.append({"class":"non-related", "sentence":"""GNC plummets after earnings miss and lowered outlook"""})
training_data.append({"class":"non-related", "sentence":"""Facebook shares hit new all-time high as Street cheers earnings"""})
training_data.append({"class":"non-related", "sentence":"""The earnings themselves were not the biggest PayPal surprise, Jim Cramer says"""})
training_data.append({"class":"non-related", "sentence":"""Harman shares slide after earnings disappoint"""})
training_data.append({"class":"non-related", "sentence":"""Truck sales drive record results at Ford; shares surge"""})
training_data.append({"class":"non-related", "sentence":"""Ahead of Amazon earnings, this analyst warns Google: Jeff Bezos is coming for you"""})
training_data.append({"class":"non-related", "sentence":"""Viacom narrows down bidders for Paramount stake to handful: CEO"""})
training_data.append({"class":"non-related", "sentence":"""UPS profit rises on higher margins, ecommerce"""})
training_data.append({"class":"non-related", "sentence":"""New burrito, beverages help Dunkin' Brands edge past estimates"""})
training_data.append({"class":"non-related", "sentence":"""AbbVie forges deeper into cancer, as clock ticks for Humira"""})
training_data.append({"class":"non-related", "sentence":"""Facebook shatters estimates, stock rockets higher"""})
training_data.append({"class":"non-related", "sentence":"""First Solar posts quarterly profit, appoints new CEO"""})
training_data.append({"class":"non-related", "sentence":"""H&R; Block sinks on weak tax-season results"""})
training_data.append({"class":"non-related", "sentence":"""Chipotle shares slide after first ever loss on surprisingly steep sales decline"""})


print ("%s sentences in training data" % len(training_data))

words = []
classes = []
documents = []
ignore_words = ['?']
# loop through each sentence in our training data
for pattern in training_data:
    # tokenize each word in the sentence
    w = nltk.word_tokenize(pattern['sentence'])
    # add to our words list
    words.extend(w)
    # add to documents in our corpus
    documents.append((w, pattern['class']))
    # add to our classes list
    if pattern['class'] not in classes:
        classes.append(pattern['class'])

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = list(set(words))

# remove duplicates
classes = list(set(classes))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)

# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    #pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    training.append(bag)
    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    output.append(output_row)

# sample training/output
i = 0
w = documents[i][0]
print ([stemmer.stem(word.lower()) for word in w])
print (training[i])
print (output[i])

import numpy as np
import time

# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)
 
def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    #sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

def think(sentence, show_details=False):
    x = bow(sentence.lower(), words, show_details)
    if show_details:
        print ("sentence:", sentence, "\n bow:", x)
    # input layer is our bag of words
    l0 = x
    # matrix multiplication of input and hidden layer
    l1 = sigmoid(np.dot(l0, synapse_0))
    # output layer
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2

def train(X, y, hidden_neurons=10, alpha=1, epochs=50000, dropout=False, dropout_percent=0.5):

    print ("Training with %s neurons, alpha:%s, dropout:%s %s" % (hidden_neurons, str(alpha), dropout, dropout_percent if dropout else '') )
    print ("Input matrix: %sx%s    Output matrix: %sx%s" % (len(X),len(X[0]),1, len(classes)) )
    np.random.seed(1)

    last_mean_error = 1
    # randomly initialize our weights with mean 0
    synapse_0 = 2*np.random.random((len(X[0]), hidden_neurons)) - 1
    synapse_1 = 2*np.random.random((hidden_neurons, len(classes))) - 1

    prev_synapse_0_weight_update = np.zeros_like(synapse_0)
    prev_synapse_1_weight_update = np.zeros_like(synapse_1)

    synapse_0_direction_count = np.zeros_like(synapse_0)
    synapse_1_direction_count = np.zeros_like(synapse_1)
        
    for j in iter(range(epochs+1)):

        # Feed forward through layers 0, 1, and 2
        layer_0 = X
        layer_1 = sigmoid(np.dot(layer_0, synapse_0))
                
        if(dropout):
            layer_1 *= np.random.binomial([np.ones((len(X),hidden_neurons))],1-dropout_percent)[0] * (1.0/(1-dropout_percent))

        layer_2 = sigmoid(np.dot(layer_1, synapse_1))

        # how much did we miss the target value?
        layer_2_error = y - layer_2

        if (j% 10000) == 0 and j > 5000:
            # if this 10k iteration's error is greater than the last iteration, break out
            if np.mean(np.abs(layer_2_error)) < last_mean_error:
                print ("delta after "+str(j)+" iterations:" + str(np.mean(np.abs(layer_2_error))) )
                last_mean_error = np.mean(np.abs(layer_2_error))
            else:
                print ("break:", np.mean(np.abs(layer_2_error)), ">", last_mean_error )
                break
                
        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)

        # how much did each l1 value contribute to the l2 error (according to the weights)?
        layer_1_error = layer_2_delta.dot(synapse_1.T)

        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
        
        synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
        synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))
        
        if(j > 0):
            synapse_0_direction_count += np.abs(((synapse_0_weight_update > 0)+0) - ((prev_synapse_0_weight_update > 0) + 0))
            synapse_1_direction_count += np.abs(((synapse_1_weight_update > 0)+0) - ((prev_synapse_1_weight_update > 0) + 0))        
        
        synapse_1 += alpha * synapse_1_weight_update
        synapse_0 += alpha * synapse_0_weight_update
        
        prev_synapse_0_weight_update = synapse_0_weight_update
        prev_synapse_1_weight_update = synapse_1_weight_update

    now = datetime.datetime.now()

    # persist synapses
    synapse = {'synapse0': synapse_0.tolist(), 'synapse1': synapse_1.tolist(),
               'datetime': now.strftime("%Y-%m-%d %H:%M"),
               'words': words,
               'classes': classes
              }
    synapse_file = "synapses.json"

    with open(synapse_file, 'w') as outfile:
        json.dump(synapse, outfile, indent=4, sort_keys=True)
    print ("saved synapses to:", synapse_file)

X = np.array(training)
y = np.array(output)

start_time = time.time()

train(X, y, hidden_neurons=20, alpha=0.1, epochs=100000, dropout=False, dropout_percent=0.2)

elapsed_time = time.time() - start_time
print ("processing time:", elapsed_time, "seconds")

# probability threshold
ERROR_THRESHOLD = 0.2
# load our calculated synapse values
synapse_file = 'synapses.json' 
with open(synapse_file) as data_file: 
    synapse = json.load(data_file) 
    synapse_0 = np.asarray(synapse['synapse0']) 
    synapse_1 = np.asarray(synapse['synapse1'])

def classify(sentence, show_details=False):
    results = think(sentence, show_details)

    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD ] 
    results.sort(key=lambda x: x[1], reverse=True) 
    return_results =[[classes[r[0]],r[1]] for r in results]
    print ("%s \n classification: %s" % (sentence, return_results))
    return return_results

#classify("Coach's profit jumps 8.6% topping Street Views, on less discounting")
#classify("Amazon surges on big earnings and sales beat")
#classify("Apple sells Iphones")
#classify("who are you?")
#classify("make me some lunch")
#classify("how was your lunch today?")
#print()
classify("SeaWorld", show_details=True)
'''
import mysql.connector

cnx = mysql.connector.connect(user='root',password='Jumeirah198', database='articles')
cursor = cnx.cursor()

query = ("SELECT * FROM articles.Article")

cursor.execute(query) 
'''
