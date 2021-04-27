# Shoolu Label Printing Scripts

## Warehouse Shelf Locations

1. To print new Labels for the Warehouse Shelf Locations, run `location-print.py`.
2. Type in your location and press Enter. Do this for all your desired locations.
3. Type in the letter 'p' and press Enter. This opens up a text file with some gibberish.
4. Print that Text File to the ZT400 Label Printer. 

## Product UPC / EAN Labels
1. To print new UPCs for products, run `sku-upc-reprint-cli.py`.
2. Type in the SKU for the product, press Enter.
3. Type in the UPC for the product, press Enter.
4. Repeat 2-3 for all the products, up to 7.
5. If you enter in 7 UPCs, the text file will open automatically. If you're making less than 7 labels, type in the letter 'p' and press Enter. This opens up a text file with some gibberish.
6. Print that Text File to the ZT400 Label Printer. 

## Update The Scripts
1. Open the `label-printing` folder and double click on the `updateLabels.sh` file. 