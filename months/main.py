if __name__ == "__main__":
 years = 0

 principal = int(input("enter the amount($):"))

 rate = int(input("enter the rate(%):"))

 amount= principal*2 
 
 t = (1/rate)*(amount/principal-1)
 months = round(t*12)
 print(f"it will take {months} months(s) for the amount to double")