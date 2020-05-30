''' Most efficient way to compute gcd. Very often, in order to find a better algorithm for a problem, 
    you need to understand something interesting about the structure of the solution, 
    and that will allow you to simplify things a lot.
    
    By Lemma, let a' be the remainder when a is divided by b, then gcd(a,b) = gcd(a',b) = gcd(b,a')
    
    e.g, gcd(357,234) =
         gcd(234,123) [As 357%234 = 123] =
         gcd(123,111) =
         gcd(111,12)  =
         gcd(12,3)    =
         gcd(0,3).....hence the ans is 3. We are able to compute it in 5 steps.
         
         Similarly a six-digit or higher digit numbers take less time to compute.
         No. of steps taken = log(ab) as number is reduced by factor of 2 in every step '''

def gcd(a,b):
    if b == 0:
        return a
    else:
        rem = a%b
        return gcd(b,rem)

if __name__ == "__main__":
    a,b = map(int,input().split())
    print(gcd(a,b))
         
