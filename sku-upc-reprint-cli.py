import webbrowser
import json

#edit the data


def printLabels(labels):

    print(labels)

    zpl_str = "${ "
    #^PW440 sets the print width to 2.2 inches(440 dots)
    zpl_str += "^XA ^PW800\n\n^CF0,25"
    marker = 40

    for index in range(len(labels)):
        #add sku to label
        zpl_str += "^^FO20,"+str(marker)+"^FB400,2,0,L^FD" + \
            str(labels[index]['sku'])+"^FS\n\n"
        #barcode string
        marker = marker + 50
        zpl_str += "^BY3,2,100^FO20,"+str(marker)+"^BC^FD" + \
            str(labels[index]['upc']) + "^FS\n\n"
        #end zpl
        marker = marker + 185

    zpl_str += "\n\n^XZ"
    #end for loop
    #end zpl command
    zpl_str += "}$"
    #write the text file to print
    label_path = ".\\sku-upc-labels_results.txt"
    label_file = open(label_path, "w")
    label_file.write(zpl_str)
    label_file.close()

    webbrowser.open(label_path)


labels = []

while True:    # infinite loop
    print(str(len(labels)) + " Labels To Print")
    if len(labels) != 7:
        sku = input("Enter your sku ('p' to Print or 'q' to quit): ") 
        if sku == "q":  
            break
        elif sku == "p" or sku == "print":
            printLabels(labels)
            labels = []
        elif sku =="":
            sku = ''
        else :
            upc = input("Enter the UPC : ") 
            labels.append({"sku": sku, "upc": upc})
    else:
        printLabels(labels)
        labels = []


