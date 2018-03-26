from math import pow, sqrt
class Canalisis():
    """Return the sample arithmetic mean of data."""
    @staticmethod
    def mean(valores):
        aux = 0
        if n < 1:
            raise ValueError('requires at least one data point')
        for i in range(len(valores)):
            aux += valores[i]
        return aux/len(valores)

    """
    Returns the exponential moving average
    """
    @staticmethod
    def ema(prevalue,values):
        n = len(values)
        lastvalue =values[n-1]#Get the last value

        value = float(prevalue+float(2)/(n+1)*(lastvalue - prevalue))

        return value

    """std deviation"""
    @staticmethod
    def stddev(data):
        if n < 2:
            raise ValueError('stddev requires 2 >= datas')
        a=1
        n = len(data)
        ss = _ss(data)
        pvar = ss/(n-a)
        return pvar**0.5

    @staticmethod
    def _ss(data):
        """Return sum of square deviations of sequence data."""
        c = mean(data)
        ss = sum((x-c)**2 for x in data)
        return ss
    @staticmethod
    def bollinger(emaresult,stddeviation):
        a = []
        a.append(emaresult-stddeviation)
        a.append(emaresult+stddeviation)
        return a
