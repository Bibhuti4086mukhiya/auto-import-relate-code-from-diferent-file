def buyerAndbid(bidder_list):
    buyer=bidder_list.pop(0)
    buyerBid=bidder_list.pop(0)
    return buyer,buyerBid
def buyerAndbidRead(bidder_list):
    buyer=bidder_list[0]
    buyerBid=bidder_list[1]
    return buyer,buyerBid
def main(inputVal):
    bidder_list=inputVal.split(',')
    open_price=bidder_list.pop(0)
    first_bid=1
    highest_bid=''
    highest_bidder=''
    bidder=''
    bid=''
    buyer=[]
    for i in range(0,(len(bidder_list)),2):
        buyer+=[bidder_list[i]]
    for i in buyer:
        if bidder_list[0]==i:
            p=True
        else:
            p=False
            break
    if p==True:
        return bidder_list[0],open_price
    for i in range((len(bidder_list)//2)-1):
        if len(bidder_list)!=0:
            if len(bidder_list)!=0:
                bidder1,bid1=buyerAndbid(bidder_list)
            if len(bidder_list)!=0:
                bidder2,bid2=buyerAndbidRead(bidder_list)
            if i==0:
                bidder=bidder.replace(bidder,bidder1)
                bid=bid.replace(bid,open_price)
                highest_bid=highest_bid.replace(highest_bid,str(bid))
                highest_bidder=highest_bidder.replace(highest_bidder,bidder)
                if len(bidder_list)==0:
                    break
            if int(bid1)<int(bid2) and bidder1!=bidder2:
                bidder=bidder.replace(bidder,bidder2)
                bid=bid.replace(bid,str(int(bid1)+int(first_bid)))
                if int(highest_bid)<int(bid2):
                    bid=highest_bid.replace(highest_bid,str(bid))
                    bidder=highest_bidder.replace(highest_bidder,bidder)
                if int(highest_bid)>int(bid1) and int(highest_bid)>int(bid2):
                    bidder=bidder.replace(bidder,highest_bidder)
                    bid=bid.replace(bid,str(int(bid2)+int(first_bid)))
                if int(bid1)>int(highest_bid) and int(bid2)>int(highest_bid):
                    highest_bidder=highest_bidder.replace(highest_bidder,bidder2)
                    highest_bid=highest_bid.replace(highest_bid,str(int(bid2)+int(first_bid)))
            if int(bid1)>int(bid2)and bidder1!=bidder2:
                bidder=bidder.replace(bidder,bidder1)
                bid=bid.replace(bid,str(int(bid2)+int(first_bid)))
                if int(highest_bid)<int(bid):
                    highest_bid=highest_bid.replace(highest_bid,str(bid1))
                    highest_bidder=highest_bidder.replace(highest_bidder,bidder)
            if int(bid1)==int(bid2) and bidder1!=bidder2:
                bidder=bidder.replace(bidder,bidder1)
                bid=bid.replace(bid,str(int(bid1)))
                if int(highest_bid)<int(bid):
                    highest_bid=highest_bid.replace(highest_bid,str(bid1))
                    highest_bidder=highest_bidder.replace(highest_bidder,bidder)
            if bidder1==bidder2:
                if int(bid1)>int(bid2):
                    bidder=bidder.replace(bidder,bidder2)
                    bid=bid.replace(bid,str(int(highest_bid)+int(first_bid)))
                    highest_bidder=highest_bidder.replace(highest_bidder,bidder)
                if int(bid1)<int(bid2):
                    bidder=bidder.replace(bidder,bidder1)
                    bid=bid.replace(bid,str(int(bid2)+int(first_bid)))
                if int(highest_bid)>int(bid1) and int(highest_bid)>int(bid2):
                    bid=bid.replace(bid,str(int(bid2)+int(first_bid)))
                    bidder=bidder.replace(bidder,highest_bidder)
                if int(bid1)>int(highest_bid) and int(bid2)>int(highest_bid):
                    bid=bid.replace(bid,highest_bid)
                    bidder=bidder.replace(bidder,highest_bidder)
    return bidder,bid
print("aaa")
print(main("100,C,100"))