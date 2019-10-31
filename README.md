# sibyl
References: https://www.quantstart.com/articles/Best-Programming-Language-for-Algorithmic-Trading-Systems

0. Architecture
- Creating a component map of an algorithmic trading system is worth an article in itself. However, an optimal approach is to make sure there are separate components for the historical and real-time market data inputs, data storage, data access API, backtester, strategy parameters, portfolio construction, risk management and automated execution systems.

Another benefit of separated components is that it allows a variety of programming languages to be used in the overall system. There is no need to be restricted to a single language if the communication method of the components is language independent. This will be the case if they are communicating via TCP/IP, ZeroMQ or some other language-independent protocol.

As a concrete example, consider the case of a backtesting system being written in C++ for "number crunching" performance, while the portfolio manager and execution systems are written in Python using SciPy and IBPy.


Required components

1. Research + Backtesting
- Points of emphasis: available libraries + performance


2. Portfolio construction + Risk management (Strategies)
-  A frequently rebalanced portfolio will require a compiled (and well optimised!) matrix library to carry this step out, so as not to bottleneck the trading system.

- Risk management is another extremely important part of an algorithmic trading system. Risk can come in many forms: Increased volatility (although this may be seen as desirable for certain strategies!), increased correlations between asset classes, counter-party default, server outages, "black swan" events and undetected bugs in the trading code

3. Execution system
- The job of the execution system is to receive filtered trading signals from the portfolio construction and risk management components and send them on to a brokerage or other means of market access. For the majority of retail algorithmic trading strategies this involves an API or FIX connection to a brokerage such as Interactive Brokers. The primary considerations when deciding upon a language include quality of the API, language-wrapper availability for an API, execution frequency and the anticipated slippage.

- The "quality" of the API refers to how well documented it is, what sort of performance it provides, whether it needs standalone software to be accessed or whether a gateway can be established in a headless fashion (i.e. no GUI). In the case of Interactive Brokers, the Trader WorkStation tool needs to be running in a GUI environment in order to access their API.

Most APIs will provide a C++ and/or Java interface. It is usually up to the community to develop language-specific wrappers for C#, Python, R, Excel and MatLab. Note that with every additional plugin utilised (especially API wrappers) there is scope for bugs to creep into the system. Always test plugins of this sort and ensure they are actively maintained. A worthwhile gauge is to see how many new updates to a codebase have been made in recent months.

- Execution frequency is of the utmost importance in the execution algorithm. Note that hundreds of orders may be sent every minute and as such performance is critical. Slippage will be incurred through a badly-performing execution system and this will have a dramatic impact on profitability.

- Statically-typed languages (see below) such as C++/Java are generally optimal for execution but there is a trade-off in development time, testing and ease of maintenance. Dynamically-typed languages, such as Python and Perl are now generally "fast enough". Always make sure the components are designed in a modular fashion (see below) so that they can be "swapped out" out as the system scales.