Let’s break down **Task 2: Stock Portfolio Tracker** into detailed steps so you can build it incrementally. This task involves creating a tool that manages stock investments and fetches real-time stock data using financial APIs.

---

### **Step 1: Understand the Requirements**
The tool should:
1. Allow users to **add** stocks to their portfolio.
2. Allow users to **remove** stocks from their portfolio.
3. Display real-time information about the stocks (e.g., current price, percent change).
4. Summarize the performance of the entire portfolio.

---

### **Step 2: Set Up the Environment**
1. Install the required Python libraries:
   - **`requests`**: To fetch real-time stock data from APIs.
   - **`json`**: To parse API responses.
   - **`prettytable`** (optional): For displaying the portfolio in a table format.

2. Ensure you have access to a financial API, such as:
   - [Alpha Vantage](https://www.alphavantage.co/)
   - [Yahoo Finance API](https://rapidapi.com/apidojo/api/yahoo-finance1)
   - [Finnhub](https://finnhub.io/)

   You’ll need to:
   - Create an account.
   - Get an API key to access stock data.

---

### **Step 3: Design the Program Flow**
The program will have the following key components:

1. **Menu Options:**
   - Add a stock to the portfolio.
   - Remove a stock from the portfolio.
   - View the current portfolio and stock performance.
   - Exit the program.

2. **Portfolio Data Structure:**
   - Use a Python dictionary or list to store the portfolio. Example:
     ```python
     portfolio = {
         "AAPL": {"shares": 10, "purchase_price": 145.0},
         "TSLA": {"shares": 5, "purchase_price": 700.0},
     }
     ```

3. **Real-Time Stock Data:**
   - Fetch the stock's current price and other relevant details (e.g., percent change, market cap) using the API.

---

### **Step 4: Implement Portfolio Actions**
#### 1. **Adding a Stock:**
   - Ask the user for:
     - Stock ticker symbol (e.g., AAPL for Apple).
     - Number of shares purchased.
     - Purchase price (optional if not fetching historical data).
   - Add the stock details to the portfolio.

#### 2. **Removing a Stock:**
   - Ask the user for the stock ticker symbol to remove.
   - Remove the stock from the portfolio if it exists.

#### 3. **Viewing the Portfolio:**
   - Loop through the portfolio to display:
     - Stock ticker.
     - Number of shares.
     - Purchase price.
     - Current price (fetched from the API).
     - Total value (calculated as `shares * current price`).
   - Optionally, calculate and display:
     - Percentage change in value.
     - Total portfolio value.

---

### **Step 5: Fetch Real-Time Stock Data**
1. Use the API to fetch details for a given stock ticker.
2. Parse the API response to extract:
   - Current stock price.
   - Percentage change in price (optional).
   - Any additional details you want to display.

---

### **Step 6: Calculate Portfolio Metrics**
- For each stock in the portfolio:
  - Calculate the total value of the stock (shares × current price).
  - Calculate the profit or loss since purchase.
- Calculate the total value of the entire portfolio and the overall profit or loss.

---

### **Step 7: Build the User Interface**
- Use a simple **text-based menu** for now:
  1. Display options to the user (Add, Remove, View Portfolio, Exit).
  2. Accept input and perform the corresponding action.
- Display portfolio details in a clean and readable format (e.g., using `prettytable`).

---

### **Step 8: Add Error Handling**
1. Handle API errors (e.g., invalid stock ticker, API limits).
2. Handle invalid user inputs (e.g., non-existent ticker for removal).
3. Ensure graceful handling of edge cases (e.g., empty portfolio).

---

### **Step 9: Finalize and Test**
- Test the program by:
  1. Adding multiple stocks.
  2. Removing stocks.
  3. Viewing the portfolio to ensure correct calculations and real-time data fetching.
- Check for edge cases like:
  - Adding a stock that’s already in the portfolio.
  - Removing a stock not in the portfolio.

---

### **Step 10: Enhance the Tool (Optional)**
1. Save the portfolio data to a file (e.g., JSON or CSV) to persist between runs.
2. Allow the user to load a previously saved portfolio.
3. Add a feature to visualize portfolio performance using libraries like `matplotlib`.

---

Let me know which step you’d like to start with, and I’ll guide you in detail for that part! 😊