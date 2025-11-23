import os
import time

while True:
    barrier = "=" * 30
    barrier2 = "-" * 30

    print(f"{barrier}\n ZYGMACORE BILLING ESTIMATOR\n{barrier}\n")

    total = 0
    base = 0
    plan = input("Selected Plan (1. Basic, 2. Pro, 3. Enterprise): ")
    if plan == "1":
        plan = "Basic"
        total += 19
    elif plan == "2":
        plan = "Pro"
        total += 49
    elif plan == "3":
        plan = "Enterprise"
        total += 99
    else:
        print("Plan Unavailable.")
        break

    total_user = input("Input Total User: ")
    if total_user.isdigit():
        total_user = int(total_user)
        if total_user < 1:
            print("Input must not be zero or less.")
            break
        else:
            total *= total_user
            base = total
    else:
        print("Input must number.")
        break

    extra_storage = input("Extra Storage : $5/50GB (Input Storage): ")
    storage = extra_storage
    if extra_storage.isdigit():
        extra_storage = float(extra_storage)
        extra_storage //= 50
        extra_storage *= 5
        total += extra_storage
    else:
        print("Input must number.")
        break

    priority_bill = 0
    priority_support = input("Priority Support $15/Month (Y/N): ").lower()
    if priority_support == "y":
        priority_bill = input("for how many months? ")
        if priority_bill.isdigit():
            priority_bill = int(priority_bill)
            if priority_bill < 1 or priority_bill > 12:
                print("Input must among 1-12.")
                break
            elif priority_bill == 1:
                total += 15
                priority_bill *=15
                priority_support = "Yes"
            else:
                priority_bill *= 15
                priority_support = "Yes"
        else:
            print("Input must number.")
            break
    elif priority_support == "n":
        priority_bill = 0
        priority_support = "No"
    else:
        print("Input must Y or N.")
        break


    annual_total = 0
    billing_type = ""
    annual_billing = input("Annual Billing? (Y/N): ").lower()
    if annual_billing == "y":
        annual_total += (total * 12 + priority_bill) * (80/100)
        annual_billing = "Yes"
        billing_type = "Annual (20% Discount)"
    elif annual_billing == "n":
        annual_billing = "No"
        billing_type = "Monthly"
    else:
        print("Input must Y or N.")
        break

    os.system("clear")
    # ---
    print(f"{barrier}\n ZYGMACORE BILLING ESTIMATOR\n{barrier}\n")
    print(f"Selected Plan : {plan}")
    print(f"Number of Users : {total_user}")
    print(f"Extra Storage : {storage}GB")
    print(f"Priority Support : {priority_support}")
    print(f"Billing Type : {billing_type}\n")
    print(barrier2)
    print(f"Base Cost : ${base}")
    print(f"Storage Add-On : ${extra_storage}")
    print(f"Priority Support : ${priority_bill}")
    print(barrier2, "\n")
    if annual_billing == "No":
        print(f"Monthly Total : ${total:.2f}")
    else:
        print(f"Annual Total : ${annual_total:.2f}")
    print(barrier, "\n")
    print(f"Thank you for using ZygmaCore Billing Estimator!\n")
    print(f"Generated at: {time.localtime().tm_hour}:{time.localtime().tm_min}")

    print(barrier2, "\n")

    retry = input("Wanna use ZygmaCore Billing Estimator Again? (Y/N) ")
    if retry == "y":
        continue
    else:
        break