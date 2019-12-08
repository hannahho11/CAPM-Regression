'''please write a program that takes in a stock and requested dates and returns an estimate of the beta
(and whether it is statistically significantly different from the market's beta), and the alpha (and whether
 it is statistically significantly different from zero).  It should also supply the SCL (security characteristic line)
 and any other metrics of interest (typically, a table of summary statistics, ANOVA, and coefficients).
 It should also write all the data to an Excel file in the event the user wants to do further analysis.

Thus, one suggested procedure would be:

-Program should query the user to enter the number of stocks to analyze and dates of interest (start/end).
-Then for that number, user should enter ticker symbols.  Program should also query user as to what benchmark
is appropriate (give options that user can select (like S&P 500, Russell 3000, Nasdaq, etc.) and/or invite user
to enter their own index symbol.
-Program should request user enter the appropriate risk free rate to use.
-Program should scrape the price data from yahoo, google, or any other data site (there are plenty of examples
of code on the web that you may use).
-Program should convert price data to returns, run regression, and interpret output.   Interpretations should be
printed out to display and/or file for recordkeeping--perhaps in tabular form.
-Program should write data to file--preferably a multi-tabbed excel file with each stock's regression in one tab.
 Multiple files are also acceptable.

Note:  there are code samples for yahoo and google finance extractions available on the web--feel free to use these.
Also note that yahoo uses "adjusted price" and closing price.  You should always use the adjusted price since that incorporates the effects of dividends and splits.'''