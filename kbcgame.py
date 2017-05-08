# Yeh exercise hai
# Har line of code se pehle aapko ek line mei comment mei daal kar likhna hai, ki uss line of code ka matlab kya hai
# Aap jyada comments bhi likh sakte hai, jitne jyada comments likhenge, utna aapkya fayda hoga

# User jab bhi kabhi "lifeline" likehga toh aap uske ko bhi do galat jawaab hata kar, bache hue do options dikhaoge
# Aur user se dobara input loge.
# Kaunse galat jawaab hatane hai uske liye aap saare options ko ek ek karke iterate karo, aur ek sahi aur ek galat answer ko dikhao
# Yeh karne ke liye aapko temporary variables use karne padenge jaise aapne peechle program mei kiye the

# User uske baad jo answer daalega uske basis par apna game normally chalao



question_list1 = ["Which of these sounds would you associate with the heart?",
"In 2013, where did the natural calamity known as Himalayan tsunami occur?",
"Who is the only leader to be elected Prime Minister of Pakistan three times?",
"Which of these is a term for a place where people gather for shayari and ghazals?",
"Which Character in the film Shole had said this dialogue  Itna Sannata Kyon Hai Bhai ?",
"With Which of these states do Chhattisgarh, Jharkhand and Andhra Pradesh all share their borders ?",
"According to the title of a 2013 film, what happened at Wadala ?",
"Satyanarayan vrat me kis Bhagwan ko Satyanarayan ke roop me jaana jata hai?",
"Which is the largest banana producing country in the world?",
"Which of these words means water",
"How many thousands rupee notes would your need to become a crorepati?",
"Which of these sportsmen started his carrier as a travelling ticket examiner with Indian railways?",
"The increased level of which of these causes more humidity in the air?",
"Which of terms is used to denote food that is permissible for consumption according to Islamic law?",
"Penguin, Ostrich, Emu and Kiwi have what in common?"]

list1 = ["Tring Tring", "Uttrakhand", "Syed Yousaf Raza Gillani", "Rukhsar", "Shanbhu Kaka", "Madhya Pradesh","Meeting",
"Shiv", "Brazil", "Rahul", "100", "Bhuvneshwar Kumar", "Dust", "Jhatka", "Similar shapes"]

list2 = ["Tap Tap", "Arunachal Pradesh", "Benazir Bhutto", "Mushaira", "Rahem Kaka", "Odisha", "Romance",
"Brahma", "India", "Sanjay", "1000", "Shikhar Dhawan", "Water vapour", "Haram", "Can not fly"]

list3 = ["Click Click", "Jammu and Kashmir", "Liaqat Ali Khan", "Shikara", "Shokat Bhai", "Bihar", "Shootout",
"Ganesh", "Mexico", "Varun", "10000", "Ravinder Jadeja", "Smoke", "Halal", "Can not walk"]

list4 = ["Dhak Dhak", "Sikkim", "Nawaz Sharif", "Mahabara", "Ramu Kaka", "Uttar Pradesh", "Marriage",
"Vishnu", "China", "Rajiv", "100000", "Mahendra Singh Dhoni", "Sunlight", "Kosher", "Can not see"]



var = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th']#
answers =[4,1,4,2,2,2,3,4,2,3,4,4,2,3,2]# this our anser key
prize = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]# these is prize list
padaav = [0,0,0,0,10000,10000,10000,10000,10000,320000,320000,320000,320000,320000,10000000]# this the padaav
counter = 0
answer = ['Dhak Dhak', 'Uttrakhand', 'Nawaz Sharif', 'Mushaira', 'Rahem Kaka', 'Odisha', 'Shootout',
'Vishnu', 'India', 'Varun', '100000', 'Mahendra Singh Dhoni', 'Water vapour', 'Halal', 'Can not fly']

import random



flag=True  # agar value true hoga to python agge chalegi
for index in range(15):  #  ye loop h isme ek ek kar ke print honge
    if flag:
        print "apka",var[index],"question hai yeh"# ye question no dalne ke liye use kiya hai
        print ""# ye line ke space ke liye hai
        print question_list1[index] # this is the questions list
        print "1 - " + list1[index]# these is our option 1 list
        print "2 - " + list2[index]# these is our option 2 list
        print "3 - " + list3[index]# these is our option 3 list
        print "4 - " + list4[index]# these is our option 4 list
        print ""# this is for line space
        question_int = raw_input("answer  1, 2, 3 and 4 mei kariye:\n")# ye user se answer dalwne ke liye use kiya h
        number_times = 2
        options_list = [list1[index],list2[index],list3[index],list4[index]]
        if question_int == "lifeline":
            random_items = random.sample(options_list,number_times)


            print "1" + answer[index]
            if random_items[0] == [index]:
                print "2" +random_items[1]

            else:
                print "2" +random_items[0]
            user_input = raw_input("enter a answer''\n")

            if "quit" == user_input:
                flag=False
                print "Aap ne game se quit kar liya hai"
            elif 1 == int(user_input):

                counter = counter + 1
                print "Congrats, Sahi jawaab!"
            else:
                print "Afsos, par yeh galat jawaab hai!"


        elif question_int == "quit": # agar user quit likhega to game wo par hi ruk jaegi
            flag=False# ye hamne game ko stop hone ke liye dala h taki game waha par ruk jae

            print "Aap ne game se quit kar liya hai. Par aaj aap ghar le kar ja rahe hai", prize[index] ,"rupees."# game ko quit karte hi ye line show hogi or bategi ki abhi tak ap kitne pese jite ho


        elif int(question_int) == answer[index]:# yaha par string ko integer me change kiya h

            print "Congrats, Sahi jawaab!"# agar answer thik hoga to ye print hoga
            print prize[index] ,"R.s ap jeet chuke ho"# sahi answer hone par prize v show karega ki kitana prize milega
        else: # agar answer galt hoga to niche print hoga
            flag=False # agar value false hogi to python stop ho jaegi
            print "Galat Jawaab! Aaj aap jeet-te hai", padaav[index] ,"rupees"# agar galt hoga to ye print hoga
            print "KBC Khatam. Phir kheliyega!"
        if prize[index] == 10000:# agar prize 10000 hoga to
            print "Aapka padaav pura ho gaya hai"# ye print hhoga
            print ""
        elif prize[index] == 320000 :# agar prize 320000 hoga to
            print "Aapka doosra padaav pura ho gaya hai."# ye print hhoga
            print ""
        elif prize[index] == 10000000 :# agar prize 10000000 hoga to
            print"mubarak ho aap game jeet chuke ho aaj app ghar le ja rahe ho ek core R.sss"# ye print hhoga
            print ""
        else:# upaer walo ko chod ke kuch or ho to kuch ni hoga
            print""# jab else hoga ye ho


