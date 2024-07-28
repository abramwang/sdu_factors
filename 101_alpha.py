import model.operator as op
import pymoneta.data as data

class Alphas(object):
    def __init__(self, df_data):

        self.open = df_data['open'] 
        self.high = df_data['high'] 
        self.low = df_data['low']   
        self.close = df_data['close'] 
        self.volume = df_data['volume']
        self.returns = df_data['rtn'] 
        self.vwap = (df_data['total_turnover'])/(df_data['volume']+1) 
        
    # Alpha#1	 (rank(Ts_ArgMax(SignedPower(((returns < 0) ? stddev(returns, 20) : close), 2.), 5)) -0.5)
    def alpha001(self):
        inner = self.close
        inner[self.returns < 0] = op.stddev(self.returns, 20)
        return op.rank(op.ts_argmax(inner ** 2, 5))


def main():
    df = data.GetDayBar("stock", "*", "20210101", "20210131")
    df["rtn"] = (df["close"] - df["prev_close"])/df["prev_close"]

    #print(df)
    #print(df.columns)
    #return
    stock=Alphas(df)
    df['alpha001']=stock.alpha001() 
    print(df['alpha001'])
    print(df['alpha001'].describe())
    pass


if __name__ == "__main__":
    main()