import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from pycoingecko import CoinGeckoAPI

class CustomSalesInvoice(SalesInvoice):
    def getCryptoPrice(self):
        cg = CoinGeckoAPI()
        currency = self.currency.lower()  # Ensure it's lowercase
        
        prices = cg.get_price(ids=['bitcoin', 'ethereum'], vs_currencies=currency)

        if not prices or currency not in prices.get('bitcoin', {}) or currency not in prices.get('ethereum', {}):
            frappe.throw(f"Could not fetch cryptocurrency prices for {currency}")

        return {
            'bitcoin': self.grand_total / prices['bitcoin'][currency],    
            'ethereum': self.grand_total / prices['ethereum'][currency]
        }
