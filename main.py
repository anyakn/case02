s = 0

print('Здравствуйсте! Ответьте на следующие вопросы для расчёта НДФЛ.' )
r = input('Вы находились 183 дня в РФ за последние 12 месяцев или являютесь российским военным, служащим за границей,'
          'или сотрудником органов власти, командированным за рубеж.? ')
if r.lower()=='да':
    asset = input('Получали ли вы доход от продажи имущества? ')
    if asset.lower == 'да':
        family = input('У вас семья с двумя и более детьми и доходы от продажи объекта имущества получает несовершеннолетний ребенок из такой семьи.?')
        if asset.lower == 'да':
            asset = 0
        exemption = input('Имущество было в собственности больше трёх лет и была получена по наследству или в дар от родственников, '
                          'по договору ренты, приватизирована или это единственное жильё? ' )
        if asset.lower == 'да':
            asset = 0
        how_much = input('Имущество находится у вас в собственности менее трех или пяти лет,'
                        'при условии, что доход от продажи не превышает 1 млн руб.( для кваритиры), '
                        'а для иного имущества (гаражи, автомобили и т.д.) — 250 тыс. руб? ' )
        if asset.lower == 'да':
            asset = 0
        how_long = input('Владеете ли вы имуществом дольше 5 лет? ')
        if asset.lower == 'да':
            asset = 0
        gain = input('Продали ли вы имущество за большую сумму, чем приобрели его? ')
        if asset.lower == 'нет':
            asset = 0
        else:
            tax_base = input(' Введите сумму полученного дохода с продажи имущество '
                             '(т.е. разность между вырученной суммой и стоимости, по которой вы её приобрели изначально). ')
            asset = tax_base * 0.13
    labor = input('Получали ли вы доход от осуществления трудовой деятельности? ')
    if asset.lower == 'да':

    divident = input('Получали ли дивиденды?')
    if asset.lower == 'да':
        tax_base = input(' Введите сумму полученных дивидентов.')
        divident = tax_base * 0.13
    others = int(input('Если у вас есть другие доходы, введите их сумму.'))


else:
    asset = input('Получали ли вы доход от продажи имущества?')
    if asset.lower == 'да':
        age = int(input('Сколько полных лет находилось это имущество в собственности?'))
        if age < 5:
            asset *= 0.3
    labor = input('Получали ли вы доход от осуществления трудовой деятельности?')
    if labor.lower() == 'да':
        q1 = input('Являетесь ли вы участником Государственной программы по оказанию содействия добровольному'
                   ' переселению в РФ соотечественников, проживающих за рубежом, а также членами их семей,'
                   ' совместно переселившимися на постоянное место жительства в Российскую Федерацию?')
        q2 = input('Являетесь ли вы членом экипажей судов, плавающих под Государственным флагом Российской Федерации?')
        q3 = input('Являетесь ли вы иностранным гражданином или лицом без гражданства, признанными беженцем'
                   ' или получившим временное убежище на территории Российской Федерации')
        q4 = input('Являетесь ли вы гражданином стран-членов ЕАЭС (Армения, Белоруссия, Казахстан, Киргизия)?')
        q5 = input('Являетесь ли вы иностранным гражданином, работающим по патенту?')
        q6 = input('Являетесь ли вы иностранным гражданином, имеющим статус ВКС (высококвалифицированные специалисты)')
        if q1.lower() =='да' or q2.lower() =='да' or q3.lower() =='да'
            or q4.lower() =='да' or q5.lower() =='да' or q6.lower() =='да':
            labor = int(input('Введите сумму дохода.'))
            if labor <= 5000000:
                labor *= 0.13
            else:
                labor *= 0.15


    divident = input('Получали ли дивиденды?')
    others = int(input('Если у вас есть другие доходы, введите их сумму.'))
    others *= 0.3
s = asset+labor+divident+others





