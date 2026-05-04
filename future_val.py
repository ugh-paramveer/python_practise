#using classes

from dataclasses import dataclass
# no need to define __init__,__repr__methords



def cagr(start:float,end:float,year:int)->float:
    if start<=0 or end <=0:
        raise ValueError("value must be greater then 0")
    return (end/start)**(1/year)-1


@dataclass
class stock :
    # def __init__(self,name:str,price:float,eps_history:list[float],bv_history:list[float],low_pe=float):

    #     self.name=name
    #     self.price=price
    #     self.eps_history=eps_history
    #     self.bv_history=bv_history
    #     self.low_pe=low_pe    
    # def __init__(self): no need of this due to dataclass
    #    pass

    name:str
    price:float
    eps_history:list[float]
    bv_history:list[float]
    low_pe:float

    @property
    def eps(self)->float:
        return self.eps_history[-1]
    
    @property
    def bv(self)->float:
        return self.bv_history[-1]
    
    @property
    def eps_growth(self)->float:
        #annual groth rate (cagr)
        return cagr(self.eps_history[0],self.eps_history[-1],len(self.eps_history)-1)#mistake not just give random lenth give len(array)-1

    @property
    def bv_growth(self)->float:
        #annual groth rate (cagr)
        return cagr(self.bv_history[0],self.bv_history[-1],len(self.bv_history)-1)

        #calculating for 10 years 
    def analyze(self, year : int = 10)-> dict:
        #main calculations happen here
        #future values                                   
        fv_eps=self.eps      *(1+self.eps_growth)**year 
        fv_bv=self.bv        *(1+self.bv_growth)**year  
        fv_price=fv_eps      *self.low_pe               

        #current values
        roe_bv=         (self.eps/self.bv)*100
        roe_price=      (self.eps/self.price)*100
        future_roe_bv=  (fv_eps/fv_bv)*100
        future_roe_price=(fv_eps/fv_price)*100

        total_return=((fv_price-self.price)/self.price)*100
        annual_cagr= cagr(self.price,fv_price,year)*100

        return  {
            "current_roe_bv": round(roe_bv,2),
            "current_roe_price": round(roe_price,2),
            "future_roe_bv": round(future_roe_bv,2),
            "future_roe_price": round(future_roe_price,2),
            "future_bv":round(fv_bv),
            "future_price": round(fv_price,2),
            "future_eps": round(fv_eps,2),
            "total_return": round(total_return,2),
            "annual_cagr": round(annual_cagr,2),
        }
    
    def report(self):
        r=self.analyze()
        print(f"\n{'='*45}")
        print(f"  {self.name} — Stock Analysis")
        print(f"{'='*45}")
        print(f"  Current Price                 : ${self.price}")
        print(f"  EPS Growth (CAGR)             : {self.eps_growth*100:.2f}%")
        print(f"  BV Growth  (CAGR)             : {self.bv_growth*100:.2f}%")
        print(f"{'='*45}")
        print ("  this equity bond will provide :")
        print(f"  annual rate of return(bv)     : {r['current_roe_bv']}%")
        print(f"  annual rate of return(price)  : {r['current_roe_price']}%")
        print(f"  Future EPS (10yr)             : ${r['future_eps']}")
        print(f"  Future Price                  : ${r['future_price']}")
        print(f"  future annual rate of return(price): {r['future_roe_price']}%")
        print(f"  Total Return                  : {r['total_return']}%")
        print(f"  CAGR                          : {r['annual_cagr']}%")
        print(f"{'='*45}\n")

@dataclass
class portfolio:
    stocks:list[stock]#passing stock object

    def ranked_by_cagr(self)->list[stock]:
        return sorted(self.stocks,key=lambda x:x.analyze()["annual_cagr"],reverse=True)
    
    def result(self):
        ranked = self.ranked_by_cagr()
        print(f"\n{'='*45}")
        print(f"  Portfolio — Ranked by CAGR")
        print(f"{'='*45}")
        for i, s in enumerate(ranked, 1):
            c = s.analyze()["annual_cagr"]
            print(f"  #{i}  {s.name:20} CAGR: {c}%")
        print(f"{'='*45}\n")


if __name__=="__main__":
    ko=stock("coke",
             65.0,
             [1.60,1.65,1.95,2.06,2.17,2.37,2.57,3.02,2.93,3.49,3.85],
             [4.57,4.78,5.77,6.61,6.90,7.30,9.38,8.85,10.77,13.53,14.60],
             16.0)      
    ko.report() 
    aapl = stock("Apple", 185.0,
                 [6.13,5.61,9.01,11.89,12.30],
                 [4.25,3.84,4.06,3.06,4.25],
                 24.0)
    aapl.report()
    p=portfolio([ko,aapl])
    p.result()
   
    





