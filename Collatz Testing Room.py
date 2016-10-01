import math
print("Welcome to Collatz Testing Room!")
print("Enter 'names()' for list of utilities")

def names():
    print("Functions:\n\tHailstone\n\tFailstone\n\tPrimeExtender\n\tPrimeFactorize\n\tCompsExtender\n\tHistogram")
    print("Lists:\n\tPrimes\n\tComposites\n\tRythems")
    
def Hailstone(number,factor=False):
    "Sends the input number through the HailStone function"
    if type(number) != int or number <=0:
        print("ERR - HailStone arg. number")
        return "ERR"
    elif type(factor) != bool:
        print("ERR - HailStone arg. factor")
        return "ERR"
    else:
        while number != 1:
            if number % 2 == 0:
                number = int(number/2)
            else:
                number = int((number*3)+1)
            if factor == True:
                PrimeFactorize(number)
            else:
                print(number)

def Failstone(number,factor=1,NthPrime=1):
    "Advanced Hailstone function, number = starting value,\nfactor = 0 Factor none, 1 'odd' only, 2 factor all, \'l\' return list of odds\nNthPrime = divide 1st-->Nth prime, multiply Nth+1 prime +1"
    if type(number) != int or number <= 0:
        print("ERR - Failstone arg. number")
        return "ERR"
    elif type(NthPrime) != int or NthPrime <= 0:
        print("ERR - Failstone arg. NthPrime")
        return "ERR"
    elif factor not in [0,1,2,'l']:
        print("ERR - Failstone arg. factor")
        return "ERR"
    elif NthPrime+1 > len(Primes):
        PrimeExtender(int(2*(NthPrime+1)*math.log(NthPrime+1)))
        Failstone(number,factor,NthPrime)
    else:
        if factor != 'l':
            print("Removing primes ",Primes[0:NthPrime])
            print("Jump opperation = n *",Primes[NthPrime],"+ 1")
        if factor == 'l':
            odds = []
        fault = True
        while fault == True:
            ticker = 0
            while ticker < NthPrime:
                if number % Primes[ticker] == 0:
                    if factor == 0: #Print statments for 'even' case
                        print(number)
                    elif factor == 1:
                        print(number)
                    elif factor == 2:
                        PrimeFactorize(number)
                    elif factor == 'l':
                        pass
                    number = int(number/Primes[ticker])
                else:
                    ticker += 1
            if number != 1:
                if factor == 0: #Print statments for 'odd' case
                    print(number)
                elif factor == 1:
                    PrimeFactorize(number)
                elif factor == 2:
                    PrimeFactorize(number)
                elif factor == 'l':
                    odds.append(number)
                number = number*Primes[ticker] + 1
            else:
                if factor == 0: #Print statments for 1
                    print(number)
                elif factor == 1:
                    PrimeFactorize(number)
                elif factor == 2:
                    PrimeFactorize(number)
                elif factor == 'l':
                    odds.append(number)
                    return odds
                fault = False

#expand Primes
        
Primes = [2,3,5,7,11]            
def PrimeExtender(number):
    'Find all primes less than \'number\' and add them to Primes'
    if number < max(Primes):
        return
    else:
        print('Extending Primes...')
        if int(number + 2*math.log(number))+1 < int(len(Primes)*math.log(len(Primes)))+2:
            siftMax = int(len(Primes)*math.log(len(Primes)))+2
        else:
            siftMax = int(number + 2*math.log(number))+1
        siftMin = max(Primes) + 1
        siftRange = siftMax-siftMin

        if int(siftMax**(1/2)) > max(Primes):
            PrimeExtender(int(siftMax**(1/2))+1)

        #Set up the boolian list to be sifted
        Sifter = []
        ticker = 0
        while ticker < siftRange:
            Sifter.append(1)
            ticker += 1
            
        #populate the list of primes to use as sieve
        Sieve = []
        ticker = 0
        while int(siftMax**(1/2)) > Primes[ticker]:
            Sieve.append(Primes[ticker])
            ticker = ticker +1

        #do the sifting
        ticker0 = 0
        while ticker0 < len(Sieve):
            ticker1 = 0
            Correction = siftMin%Sieve[ticker0]
            while ticker1*Sieve[ticker0] + siftMin - Correction < siftMax:
                if ticker1 == 0 and Correction != 0:
                    pass
                else:
                    Sifter[ticker1*Sieve[ticker0]-Correction] = 0
                ticker1 +=1
            ticker0 +=1

        #add new primes to list
        ticker = 0
        found = 0
        while ticker < siftRange:
            if Sifter[ticker] == 1:
                Primes.append(siftMin+ticker)
                found +=1
            else:
                pass
            ticker +=1
        print('Found '+str(found)+' new Primes!')

def PrimeFactorize(number,output='p'):
    'Finds the prime factors of the input number\noutput = \'p\', print factorization, \'r\', return divisors list'
    if type(number) != int or number <= 0:
        print("ERR - PrimeFactorize arg. number")
        return 'ERR'
    elif output not in ['p','r']:
        print("ERR - PrimeFactorize arg. output")
        return "ERR"
    elif int(number**(1/2))+1 >= max(Primes):
        PrimeExtender(int(number**(1/2))+1)
        PrimeFactorize(number,output)
    else:
        n = number
        Divisors = []
        ticker = 0
        while n != 1:

            if int(n**(1/2))+1 < Primes[ticker]:
                prime = [int(n),1]
                Divisors.append(prime)
                n = 1
                
            elif n % Primes[ticker] == 0:
                find = [Primes[ticker],0]
                while n % Primes[ticker] == 0:
                    n = n / Primes[ticker]
                    find[1] = find[1] + 1
                Divisors.append(find)
                ticker = 0
                
            else:
                ticker += 1
        
        if output == 'p':
            print(str(number)+' ',Divisors)
        else:
            return Divisors


Composites = [[1],[1]]
def CompsExtender(number,NthPrime=1):
    'Compiles seperate lists of composites up to \'number\' for each value of \'NthPrime\'\nComposites in \'NthPrime\' list lack first \'NthPrime\' primes as factors' 
    if type(number) != int or number <= 0:
        print("ERR - CompsExtender arg. number")
        return "ERR"
    elif type(NthPrime) != int or NthPrime < 0:
        print("ERR - CompsExtender arg. NthPrime")
        return "ERR"
    elif NthPrime+1 > len(Primes):
        while NthPrime+1 > len(Primes):
            PrimeExtender(int(2*(NthPrime+1)*math.log(NthPrime+1)))
            CompsExtender(number,NthPrime)
    n = len(Composites)-1
    if n < NthPrime:
        ticker = 0
        while ticker <= (NthPrime - n):
            Composites.append([1])
            ticker += 1
        CompsExtender(number,NthPrime)
    elif number < max(Composites[NthPrime]):
        return
    elif NthPrime == 0:
        m = max(Composites[0])
        ticker = 0
        while m+ticker < number:
            Composites[0].append(m+ticker+1)
            ticker += 1
    else:
        m = max(Composites[NthPrime])
        ticker0 = 0
        while m+ticker0+1 <= number:
            ticker1 = 0
            Add = True
            while ticker1 < NthPrime and Add == True:
                if (m+ticker0+1) % Primes[ticker1] == 0:
                    Add = False
                    ticker1 += 1
                else:
                    ticker1 += 1
            if Add == True:
                Composites[NthPrime].append(m+ticker0+1)
                ticker0 += 1
            else:
                ticker0 += 1

def Histogram(MAX,MIN=1,NthPrime=1,factor=False):
    'Compiles \'odd\' hits of Hailstone numbers from MIN to MAX inclusive\nNthPrime as in func. Failstone\nWARNING: LARGE VALUES BECOME COMPUTATIONALY INTENSIVE VERY QUICKLY'
    if type(MAX) != int or MAX <= 1:
        print("ERR - Histogram arg. MAX")
        return 'ERR'
    elif type(MIN) != int or MIN < 1:
        print("ERR - Histogram arg. MIN")
        return 'ERR'
    elif MIN > MAX:
        print("ERR - Hailstone args. MIN > MAX")
        return 'ERR'
    elif type(NthPrime) != int or NthPrime < 0:
        print("ERR - Histogram arg. NthPrime")
        return "ERR"
    elif NthPrime+1 > len(Primes):
        PrimeExtender(int(2*(NthPrime+1)*math.log(NthPrime+1)))
        Histogram(MAX,MIN,NthPrime)
    elif NthPrime+1 > len(Composites):
        CompsExtender(1,NthPrime)
        Histogram(MAX,MIN,NthPrime)
    else:
        Scores = [0]
        ticker = 0
        while MIN+ticker <= MAX:
            hits = Failstone(MIN+ticker,'l',NthPrime)
            if max(hits) > max(Composites[NthPrime]):
                print("extending Comps. to",max(hits))
                print("Halistone seed",MIN+ticker,"caused extension")
                CompsExtender(max(hits)+1,NthPrime)
            while len(Scores) < len(Composites[NthPrime]):
                Scores.append(0)
            while len(hits) != 0:
                Scores[Composites[NthPrime].index(hits.pop())] +=1
            ticker +=1
        skips = 0
        ticker = 0
        while ticker < len(Scores):
            if Scores[ticker] != 0:
                if skips != 0:
                    print("\tomiting",skips,"vlaues w/->0")
                    skips = 0
                if factor == False:
                    print(str(Composites[NthPrime][ticker])+"->"+str(Scores[ticker]))
                else:
                    print(Composites[NthPrime][ticker],PrimeFactorize(Composites[NthPrime][ticker],'r'),"->",str(Scores[ticker]))
            else:
                skips +=1
            ticker +=1

Rythems = [1,[2],[4,2]]
def RhythemFinder(NthPrime):
    'under construction'
    if type(NthPrime) != int or NthPrime < 0:
        print("ERR - RhythemFinder arg. NthPrime")
        return "ERR"
    elif NthPrime+1 > len(Primes):
        PrimeExtender(int(2*(NthPrime+1)*math.log(NthPrime+1)))
        RhythemFinder(NthPrime)
    elif len(Composites) < NthPrime-1:
        CompsExtender(12,NthPrime-1)
        RhythemFinder(NthPrime)
    elif max(Composites[NthPrime]) < Primes[NthPrime]**2+Primes[NthPrime]**3-Primes[NthPrime]:
        CompsExtender((Primes[NthPrime]**2+Primes[NthPrime]**3),NthPrime)
        RhythemFinder(NthPrime)
    else:
        print("rest of function goes here")
                  
print("\nready")
