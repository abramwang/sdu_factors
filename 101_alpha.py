import model.operator as op


class Alphas(object):
    def __init__(self, df_data):

        self.open = df_data['S_DQ_OPEN'] 
        self.high = df_data['S_DQ_HIGH'] 
        self.low = df_data['S_DQ_LOW']   
        self.close = df_data['S_DQ_CLOSE'] 
        self.volume = df_data['S_DQ_VOLUME']*100 
        self.returns = df_data['S_DQ_PCTCHANGE'] 
        self.vwap = (df_data['S_DQ_AMOUNT']*1000)/(df_data['S_DQ_VOLUME']*100+1) 
        
    # Alpha#1	 (rank(Ts_ArgMax(SignedPower(((returns < 0) ? stddev(returns, 20) : close), 2.), 5)) -0.5)
    def alpha001(self):
        inner = self.close
        inner[self.returns < 0] = op.stddev(self.returns, 20)
        return op.rank(op.ts_argmax(inner ** 2, 5))


def main():
    pass


if __name__ == "__main__":
    main()