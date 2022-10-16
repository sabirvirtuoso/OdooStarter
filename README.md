# OdooStarter
A starter project on developing Odoo modules

1. Run `docker-compose up --build --detach`
2. Setup the database master credentials (you will probably do it once)
3. Login as administrator (to have the privilege to update module) and install `discuss (any other may work)` module to enable the `General Settings` tab
4. In the `Developer Tools` section click `Activate the developer mode` 
5. Navigate to `Apps` section and click on `Update Apps List` and type the module name in the search bar after cancelling the `Apps` filter.
   Your custom module should appear. 
6. Clone the version of odoo you want to create modules for and add it to source directory 
   `git clone https://github.com/odoo/odoo.git --depth 1 --branch <your-odoo-version> --single-branch odoo`
7. You can optionally initialize `Pipenv environment` in Pycharm. Refer to this [link](https://www.jetbrains.com/help/pycharm/pipenv.html)
