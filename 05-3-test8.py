with open("info.txt", 'r', encoding='utf-8') as file:
    for line in file:
        name, w, h = line.strip().split(',')
        if (not name) or (not w) or (not h):
            continue
        
        bmi = int(w) / ((int(h) / 100) ** 2)
        result = ""
        if 25 <= bmi:
            result = '과체중'
        elif 18.5 <= bmi:
            result = '정상 제충'
        else: 
            result = '저체중'
            
        print(f'이름:{name} 몸무게:{w} 키:{h}')
        print(f'BMI:{round(bmi)} 결과:{result}')