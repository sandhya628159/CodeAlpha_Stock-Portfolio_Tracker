# ==============================================================================
# 🚀 PROJECT: STOCK PORTFOLIO TRACKER (TECH INTERNSHIP EDITION)
# 
# DESCRIPTION: 
# A professional, terminal-based stock management portfolio tracking application. 
# This system handles real-time basic arithmetic calculations, verifies market asset
# mapping bounds, and generates standard spreadsheet ledger summaries automatically.
#
# KEY FEATURES:
# 1. Dictionary Market Base: Restricts token selections to strict defined asset pools.
# 2. Financial Logic Automation: Calculates total asset worth using manual multipliers.
# 3. Automatic Ledger Export: Compiles runtime summaries directly into clean CSV structures.
#
# TECHNICAL DETAILS:
# - Language: Python 3.x
# - Data Structures Used: Dictionary (for price lookup) and List Matrix (for CSV layout)
# ==============================================================================

import csv
import sys
from datetime import datetime
from typing import Dict, List

class CodeAlphaStockTracker:
    def __init__(self) -> None:
        # Core Rule Specification: Hardcoded dictionary to define stock market asset unit prices
        self.stock_market_prices: Dict[str, float] = {
            "AAPL": 180.00,
            "TSLA": 250.00,
            "MSFT": 420.00,
            "AMZN": 175.00,
            "GOOGL": 150.00
        }
        self.user_portfolio: Dict[str, int] = {}

    def display_market_prices(self) -> None:
        """Renders the fixed market asset data catalog table grid bounds cleanly."""
        print("\n--- AVAILABLE MARKET STOCKS & PRICES ---")
        for ticker, price in self.stock_market_prices.items():
            print(f" {ticker}: ${price:.2f}")
        print("-" * 40)

    def build_portfolio(self) -> None:
        """Processes dynamic input loops to cleanly update local configuration arrays."""
        self.display_market_prices()
        print("\nEnter the stocks you own to calculate total investment.")
        print("(Type 'done' anytime when you are finished adding stocks)\n")
        
        while True:
            ticker_input: str = input("Symbol (e.g., AAPL): ").strip().upper()
            
            if ticker_input == "DONE":
                break
                
            if ticker_input not in self.stock_market_prices:
                print(f"❌ '{ticker_input}' is not in our market dictionary. Choose from the list above.")
                continue
                
            try:
                quantity_input: str = input(f"Enter quantity for {ticker_input}: ").strip()
                quantity: int = int(quantity_input)
                
                if quantity <= 0:
                    print("❌ Quantity must be a positive integer calculation value.")
                    continue
                    
                self.user_portfolio[ticker_input] = self.user_portfolio.get(ticker_input, 0) + quantity
                print(f"✅ Added: {quantity} shares of {ticker_input} successfully.\n")
                
            except ValueError:
                print("❌ Invalid input! Please enter a valid whole number for dynamic share quantity.")

    def calculate_and_save_summary(self) -> None:
        """Computes financial calculations dashboard metrics and writes CSV targets."""
        if not self.user_portfolio:
            print("\n⚠️  Portfolio is empty. No tracking variables or investments logs processed.")
            return

        print("\n" + "="*55)
        print("📊 CODEALPHA PORTFOLIO INVESTMENT SUMMARY REPORT 📊")
        print("="*55)
        print(f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 55)
        print(f"{'STOCK':<10}{'QTY':<10}{'MARKET PRICE':<15}{'TOTAL VALUE':<15}")
        print("-" * 55)

        grand_total_investment: float = 0.0
        report_rows: List[List[str]] = []

        for ticker, qty in self.user_portfolio.items():
            unit_price: float = self.stock_market_prices[ticker]
            total_stock_value: float = qty * unit_price
            grand_total_investment += total_stock_value
            
            print(f"{ticker:<10}{qty:<10}${unit_price:<14.2f}${total_stock_value:<14.2f}")
            report_rows.append([ticker, str(qty), f"${unit_price:.2f}", f"${total_stock_value:.2f}"])

        print("-" * 55)
        print(f"💰 TOTAL PORTFOLIO INVESTMENT VALUE: ${grand_total_investment:.2f}")
        print("="*55)

        # Core System Concept Application: File Handling storage logic layout (.csv)
        filename: str = "portfolio_summary.csv"
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["CodeAlpha Python Internship - Stock Portfolio Summary"])
                writer.writerow(["Timestamp", datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
                writer.writerow([])
                writer.writerow(["Stock Symbol", "Quantity Owned", "Market Price Per Unit", "Total Asset Value"])
                
                for row in report_rows:
                    writer.writerow(row)
                    
                writer.writerow([])
                writer.writerow(["TOTAL PORTFOLIO VALUE", "", "", f"${grand_total_investment:.2f}"])
                
            print(f"\n💾 Success! Financial ledger records saved automatically to layout file: '{filename}'")
        except IOError:
            print("\n❌ Error! Failed to execute target data saving parameters.")

if __name__ == "__main__":
    tracker = CodeAlphaStockTracker()
    tracker.build_portfolio()
    tracker.calculate_and_save_summary()
