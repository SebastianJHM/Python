import sys
import re

def principal( argv ):
    ## Find inside []
    log = "mtmptcmpoctmptcompot [12345] k mgpmvptomgvoptmopvmt mvptgmvpt votgmpv"
    regex = r"\[(\d+)\]"
    result = re.search(regex, log)
    print(result)
    print(result[0])
    print(result[1])
    ## Find all coincidences
    text = "niejnfcn fruit froit mdcsomcos"
    x = re.findall("fr.it", text)
    print(x)
    
    x = re.search(r"aza", "plaza")
    print(x)
    
    ## Begginning whit x
    x = re.search(r"^x", "xenon")
    print(x)
    
    x = re.search(r"p.ng", "clapping")
    print(x)
    
    x = re.search(r"p.ng", "Pangea")
    print(x)
    
    x = re.search(r"p.ng", "Pangea", re.IGNORECASE)
    print(x)
    
    x = re.search(r"[Pp]ython", "Python")
    print(x)
    
    x = re.search(r"[a-z]way", "the best highway")
    print(x)
    
    x = re.search(r"cloud[a-zA-Z0-9]", "cloudy")
    print(x)
    
    x = re.search(r"cat|dog", "I love dogs")
    print(x)
    
    x = re.search(r"cat|dog", "I love cats and dogs")
    print(x)
    
    x = re.findall(r"cat|dog", "I love cats and dogs")
    print(x)
    
    ## .*: 0 or more characters between p and n
    x = re.search(r"p.*n", "pygmalion")
    print(x)
    
    x = re.search(r"p.*n", "python programmin")
    print(x)
    
    x = re.search(r"p[a-z]*n", "python programmin")
    print(x)
    
    x = re.search(r"o+l+", "woolly")
    print(x)
    
    ## ?: 0 or 1 appear of p
    x = re.search(r"\s?each", "To each their own")
    print(x)
    x = re.search(r"\s?each", "To peach their own")
    print(x)
    
    ## Search .
    x = re.search(r"\.", "woolly.")
    print(x)
    
    ##\w: alphanumerical character. Letters, number and underscore
    x = re.search(r"\w*", "this is an example")
    print(x)
    x = re.search(r"\w*", "other_example")
    print(x)
    
    ## \d: digits
    ## \s: whitespaces
    
    ## Begin and finish with a
    x = re.search(r"^A.*a$", "Argetina")
    print(x)
    x = re.search(r"^A.*a$", "Azerbajan")
    print(x)
    
    ## Begin and finish with a
    x = re.search(r"^(\w*), (\w*)", "Herrera, Sebastián")
    print(x)
    print(x.groups())
    print(x[0])
    print(x[1])
    print(x[2])
    
    ## Begin and finish with a
    x = re.search(r"[a-zA-Z]{5}", "Argetina labura tarde y noche")
    print(x)
    x = re.findall(r"[a-zA-Z]{5}", "Argetina labura tarde y noche")
    print(x)
    x = re.findall(r"\b[a-zA-Z]{5}\b", "Argetina labura de tarde y de noche")
    print(x)
    x = re.findall(r"\w{5,10}", "Argetina labura de tarde y de noche")
    print(x)
    
    ## split
    x = re.split(r"[.?!]", "mkcedmocemc. mcwomwcomc? jmsdo oommo mocdwimiowcmow1!")
    print(x)
    x = re.split(r"([.?!])", "mkcedmocemc. mcwomwcomc? jmsdo oommo mocdwimiowcmow1!")
    print(x)
    
    ## replace
    x = re.sub(r"[\w]+@[\w\.-]+", "[REDACTED]", "Recevied mail from go_nuts95@my_example.com")
    print(x)
    x = re.sub(r"^(\w*), (\w*)", r"\2 \1", "Herrera, Sebastián")
    print(x)
#fed


if __name__ == "__main__":
    principal( sys.argv )
#fi