from flask import Flask, redirect, url_for, request
import class_product.py

app = Flask(__name__) 
  
# Pass the required route to the decorator. 
if(@app.route("/products", methods=['GET'])): #fechAll
    def returnProducts():
        products = getProducts()
        for row in products:
            print("Nome: ", row[1])
            print("Marca: ", row[2])
            print("Prezzo: ", row[3])
            print("\n")
        cursor.close()
elif (@app.route("/products/<int: id>", methods=['GET'])): #fechObject
    def returnProduct:
        product = getProduct()
        print("Nome: ", row[1])
        print("Marca: ", row[2])
        print("Prezzo: ", row[3])
        print("\n")
        cursor.close()
elif (@app.route("/products/", methods=['POST'])) #create