class inventoryItem:
    itemCount = 0

    def __init__(self, sku, cost, category):
        self.sku = sku
        self.cost = cost
        self.cat = category
        inventoryItem.itemCount += 1

    def getCost(self):
        print("Our cost is ", self.cost)

    def getPrice(self):
        print("Our price is ", self.cost * 1.5)

class washer(inventoryItem):
    def __init__(self, sku, cost, frontLoad):
        inventoryItem.__init__(self, sku, cost, "Washer")
        self.fl = frontLoad
    def printType(self):
        if frontLoad:
            print("Frontload")
        else:
            print("Sideload")


class dryer(inventoryItem):
    def __init__(self, sku, cost, btus):
        inventoryItem.__init__(self, sku, cost, "Washer")
        self.btus = btus
    def printBtus(self):
        print(self.btus)


def printCost(inItem):
    print(inItem.getCost())

w = washer(123, 600, True)
d = washer(123, 500, 1200)

printCost(w)
printCost(d)
