# sales_order_history

We recommend every repository include a README, LICENSE, and .gitignore.
…or create a new repository on the command line

echo "# sales_order_history" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/leangjia/sales_order_history.git
git push -u origin master

…or push an existing repository from the command line

git remote add origin https://github.com/leangjia/sales_order_history.git
git push -u origin master

…or import code from another repository

You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

------------------------------------------------------------
Sales History Of Products in Sales Quotation and Sales Order
------------------------------------------------------------

In the sales system, it's good to have the last selling prices of the product while creating the sales order in the ERP system. The terms of last selling price will help to get the idea of the margin and sales increment and decrement process by comparing the history price with the current selling price.

The term sales history is reflected with the every customer to which the user will going to sell some product on the regular basis. It will help to track the user at what sales price the product will sell by the salesperson to that customer.

It is very helpful to get the last sales price of the product in the Odoo Sales Quotation and Sales Order itself and display it in the every product line to get its better idea of the previous sales price. 

An effort towards providing decision making information through the product’s previous sales price in Odoo, we develop the following module that will be very helpful to getting the products last two sales price in the Sales Quotation and Sales Order.

This module will give the sales price of the product from the last two Sales Order which is in the ‘Done’ state for the same particular Customer. The last two sales price of the product will display in the form view and the tree view of the order line of the Sales Quotation and Sales Order.


