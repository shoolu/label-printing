import webbrowser
import json

#edit the data


def printLabels(labels):

    print(labels)

    zpl_str = "${ "
    marker = 40

    for index in range(len(labels)):
        zpl_str += "^XA ^PW800\n\n^CF0,60"
        #add sku to label
        zpl_str += "^^FO20,225^FB300,2,0,r^FD" + str(labels[index]['location'])+"^FS\n\n"
        #barcode string
        marker = marker + 50
        zpl_str += "^BY3,2,100^FO360,200^BC^FD" + str(labels[index]['location']) + "^FS\n\n"
        #end zpl
        
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
    location = input("Enter your Location ('p' to Print or 'q' to quit): ") 
    if location == "q":  
        break
    elif location == "p" or location == "print":
        printLabels(labels)
        labels = []
    elif location =="":
        location = ''
    else :
        labels.append({"location": location})



