#После выполнения домашнего задания по определению есть ли номерные знаки в списке,
#переделать программу, таким образом,
#1 . чтоб функция получала на вход введенные данные с командной строки и
#Проверяла на соответствие Длине введенного текста
#Возвращала 6 значений полученных из введенного номера (по 2 буквы и 4 цифры)
#Если общее количество символов больше или меньше 8 (во введенных данных) возвращала False
#2. Написать вторую функцию, которая будет считать сумму чисел внутри последовательности.
#Функция должна вернуть сумму
#3.Использовать эти функции в изначальной задаче

import functions_dz

plates_list = ['HH9901CC', 'CA9150WC', 'BH7144WB', 'AI7665KU', 'AI8045DS', 'HH1233HH', 'AI1552MG', 'AI7232BO',
               'AI9224SI', 'AI5813YC', 'CA7641NN', 'HH8354IT', 'AI1631PU', 'HH2142QK', 'AI7515JS', 'HH1034SF',
               'HH8046BN', 'AI7893JE', 'BH4816PN', 'BH9195WX', 'HH1902ZE', 'CA2149DP', 'BH4079WR', 'HH3503QK',
               'BH2038DR', 'AI9892GS', 'AI6924FR', 'AI0695UE', 'HH1500TD', 'AI7201BP', 'CA6466FX', 'BH8653FG',
               'HH4226BX', 'HH1435YA', 'CA0707EO', 'BH7137OO', 'AI0841EI', 'CA3900TF', 'BH7794SH', 'HH2801XZ',
               'CA7038QP', 'HH0690BG', 'CA0525YT', 'CA4975MK', 'BH2989XM', 'CA4959YE', 'AI3287FQ', 'HH9437PS',
               'CA9181GT', 'CA0149IY', 'HH9428QC', 'AI4953VO', 'CA6865CO', 'HH1232DG', 'BH8615IF', 'AI7449IG',
               'HH3449KN', 'BH4566LG', 'HH0831CU', 'CA5707NI', 'HH0643TQ', 'HH6189GU', 'CA0121BF', 'CA0324KX',
               'BH1085ZY', 'HH6511HA', 'AI0198CN', 'CA8272PY', 'AI6526OW', 'CA6072CC', 'HH7607EL', 'HH8954WZ',
               'AI8570XO', 'BH4590NF', 'CA2556ZT', 'CA8107ZJ', 'AI0465RS', 'CA5863SV', 'AI2402VO', 'HH8841SA',
               'AI9313QU', 'HH5980CO', 'HH3448RN', 'AI2570OP', 'BH6239GW', 'BH0169KV', 'BH8429YO', 'HH8046BN',
               'BH1361VQ', 'HH5442IT', 'HH8014BO', 'HH1070BK', 'HH6262IE', 'BH4293SN', 'HH8002ZY', 'AI0380IH',
               'CA8077IQ', 'CA2727LR', 'CA7798IP', 'BH9536GJ', 'HH2243KF', 'CA5269CC', 'HH5154TA', 'HH0513GL',
               'HH4824HI', 'BH1528MK', 'CA1139CA', 'BH1087IO', 'AI0482SK', 'HH5308CG', 'AI9000ZR', 'HH2240DH',
               'CA8908GL', 'HH3930SO', 'CA0815CD', 'BH4064PB', 'HH1601DN', 'CA9575UW', 'CA4512PO', 'BH7937GM',
               'HH5158GZ', 'CA3916LU', 'AI9048HQ', 'HH8200VI', 'CA7380HP', 'CA6346NC', 'BH6516ZD', 'AI4955SG',
               'AI8980BR', 'BH6831UL', 'HH7033HS', 'AI9299CL', 'HH1489LY', 'AI8594VW', 'HH0875IT', 'AI4820AZ',
               'AI3312UQ', 'AI8552BN', 'HH6553GK', 'HH8113ZL', 'AI5421QU', 'AI0543HL', 'BH1415XI', 'CA9741LA',
               'HH1024BE', 'CA5733QR', 'BH3849GW', 'CA0251MV', 'BH4087ZY', 'HH2494JS', 'CA9552VE', 'CA3036YH',
               'HH5897DO', 'BH3151PI', 'CA9217QK', 'AI9684IL', 'HH9564WI', 'AI6701IO', 'AI3651IX', 'BH5526BN',
               'BH7770EJ', 'CA8940EY', 'HH3573NN', 'AI3081UG', 'CA8269RB', 'AI3810UD', 'BH2660OL', 'AI5225TW',
               'BH2634YT', 'AI5602RC', 'BH0843RB', 'CA1001QC', 'CA9061KG', 'HH8702UZ', 'HH8317JR', 'HH4225KB',
               'CA0316AO', 'HH2761XT', 'HH4532OM', 'CA5595ZT', 'BH0215MR', 'HH1586TE', 'HH0247RV', 'HH1152XZ',
               'HH6687WD', 'BH3097UC', 'CA6650VC', 'CA4463GM', 'HH3393NC', 'BH4728NW', 'BH6118VL', 'CA8416VH',
               'AI2453JZ', 'BH8988SR', 'BH0519PS', 'HH7551YB', 'HH0299BA', 'AI5909OM', 'BH0093RS', 'CA8305IZ',
               'CA2332OF', 'CA6712HD', 'CA6292TO', 'CA8983SR', 'BH7003UA', 'BH6022LU', 'CA2148PB', 'HH7191ZM',
               'HH0846SE', 'HH2534IR', 'AI7261ZR', 'BH2714GL', 'HH8326GG', 'AI0310YT', 'AI6999DR', 'BH0640GY',
               'HH4546MS', 'AI1322GD', 'BH1602IO', 'HH8991CE', 'HH7223CZ', 'AI6848CU', 'AI4734UD', 'AI3491ND',
               'HH1753JZ', 'HH2522BE', 'AI9218AV', 'CA0738XV', 'AI8837WE', 'AI5126YT', 'CA1386LD', 'CA0722YF',
               'HH4135WT', 'CA2941HJ', 'BH3118XG', 'AI0043VB', 'CA3497AW', 'BH8339OP', 'CA6491FC', 'AI6120FM',
               'BH5411UA', 'CA5259KF', 'AI8242FN', 'HH9723IB', 'BH7456YH', 'HH0603UF', 'HH9681KG', 'CA9502HB',
               'BH5421NC', 'AI8193CA', 'CA0307MQ', 'BH3047HZ', 'HH1824TJ', 'CA8592ML', 'AI9196WK', 'BH9099GU',
               'HH3448HH', 'HH2319OP', 'BH3028RS', 'AI5851BK', 'HH7316YE', 'AI5002EQ', 'CA5243DO', 'AI6057DZ',
               'BH9461GX', 'AI5102OG', 'BH1786CG', 'HH5379CW', 'BH0598KV', 'HH5136EM', 'HH0676ZO', 'HH8820NP',
               'BH1026KH', 'AI6908OS', 'HH5633KS', 'HH9443PT', 'BH0410LM', 'HH9684NP', 'BH2056RA', 'HH2093CL',
               'CA6675BB', 'AI3178NS', 'CA1542SQ', 'HH5372CB', 'CA4481DG', 'BH4165NO', 'BH4114YT', 'CA7138KZ',
               'BH1932EV', 'HH9530VO', 'AI4958EQ', 'AI2427CY', 'CA5291CK', 'AI9210IE', 'CA6845XJ', 'CA2238GC',
               'AI8801UU', 'HH5274LF', 'HH3727MX', 'AI1360KN', 'AI9133YL', 'AI9030DY', 'BH5152SW', 'CA5091BJ',
               'AI3055PO', 'CA8901BT', 'CA2797FQ', 'HH4897WP', 'CA6242SR', 'CA7213BD', 'AI5214PC', 'HH5468SY',
               'CA8518KN', 'AI7592TP', 'CA2290BR', 'HH2260IQ', 'HH1226LC', 'HH9530HK', 'HH2881MB', 'AI8760NT',
               'BH2379UR', 'HH1840NI', 'AI8600LB', 'HH8813XQ', 'HH9337TW', 'CA6778RI', 'CA4632DY', 'HH1743UQ',
               'HH4396ZY', 'CA5808LX', 'HH6000WZ', 'HH7166RR', 'HH4750EV', 'BH7340HZ', 'CA1405GF', 'CA2072UD',
               'BH8884DZ', 'HH3060CX', 'AI7320TU', 'CA1354FU', 'BH9131NT', 'BH7191TW', 'HH7322XZ', 'HH3449ME',
               'AI9373AP', 'BH0826GV', 'HH2296CL', 'CA3745JL', 'CA7540LG', 'HH2618RA', 'BH9721BU', 'AI5984LC',
               'AI7622HW', 'HH2759IC', 'BH5823CQ', 'HH8096GV', 'AI0871RH', 'BH0139RG', 'BH8227XB', 'HH1204DZ',
               'CA9172NM', 'HH2586CY', 'CA6705RF', 'AI0310QP', 'AI6836ON', 'BH0439CQ', 'CA3279JU', 'BH8727TU',
               'CA4918WH', 'AI3137LV', 'AI3201KA', 'HH9756GR', 'BH8322TM', 'HH6258SG', 'BH5456MD', 'BH3669KA',
               'AI1994DU', 'AI2308WT', 'BH0618HD', 'HH0208ZI', 'HH0612HD', 'AI1928BM', 'HH2160EA', 'AI6591LE',
               'BH3348AN', 'AI0840IU', 'CA5116NT', 'BH6224KI', 'AI8929PB', 'HH5025GU', 'CA9488UX', 'CA8461GJ',
               'AI5642WF', 'BH8434MH', 'AI4118MH', 'BH4054ON', 'BH9184WU', 'BH0216JX', 'BH3595FX', 'BH5392JA',
               'HH5537CW', 'HH2326JB', 'CA6876OJ', 'HH5101FO', 'AI8227YG', 'AI9626ZE', 'CA1276LR', 'HH5638HF',
               'BH3243VX', 'HH2773QG', 'AI1554BH', 'HH1889PV', 'HH8253FG', 'HH0122ZU', 'HH5629PE', 'AI0445PA',
               'AI5459AO', 'CA2543DS', 'CA0758RM', 'BH5126PA', 'AI3869TS', 'CA4376RD', 'HH5838LG', 'BH6073GM',
               'HH2924CZ', 'HH2863GJ', 'HH9420AZ', 'CA8245TH', 'BH4148GW', 'AI6957MW', 'CA8543FD', 'BH4657PJ',
               'HH7356WK', 'HH4784RM', 'AI6596QV', 'AI3183WH', 'BH0237CV', 'HH4062LS', 'HH0970BV', 'AI0315MP',
               'AI0137NF', 'CA2634XS', 'HH4342BI', 'CA9149YG', 'BH2737UM', 'BH3553TY', 'BH0733DZ', 'BH7858PC',
               'HH3940XE', 'BH3483TT', 'HH0325JQ', 'AI6789YL', 'HH2422NO', 'CA8377XR', 'HH5666MO', 'AI8656ZC',
               'BH6451PT', 'CA3493JS', 'AI2554XG', 'CA1940GH', 'AI0355YC', 'BH6634RW', 'CA2628GE', 'CA2166US',
               'CA7798CI', 'BH7564MH', 'AI0226TY', 'BH7619AE', 'BH0903MX', 'HH4631NC', 'HH9941HB', 'HH7357WK',
               'BH5517OX', 'CA8143MP', 'CA0394YI', 'CA8595JR', 'HH4372KT', 'BH1164EV', 'HH7743PC', 'CA7045SV',
               'CA1553EZ', 'HH2265LW', 'CA7923HZ', 'BH0961SX', 'AI2024UD', 'BH6311WU', 'AI5862TY', 'HH0638MT',
               'AI6196IQ', 'CA8869FN', 'HH7372HJ', 'BH8952GQ', 'CA2010IJ', 'HH9692QF', 'AI6044VF', 'CA4973TV',
               'HH5877JU', 'BH7692RB', 'AI4148DB', 'HH1752WM', 'BH1405KH', 'CA8840XG', 'AI7696II', 'CA1340XN',
               'HH2457SE', 'AI9824MW', 'BH2365MK', 'HH9264BH', 'AI7705RB', 'CA5351YD', 'HH9354IE', 'HH4959IO',
               'CA4129BS', 'CA4577DO', 'HH2435TI', 'CA2684BZ', 'AI1871ED', 'HH0127NL', 'AI1709CU', 'CA8874QM',
               'CA6323UL', 'HH3513MR', 'CA9287KK', 'AI1120MG', 'AI0446SY', 'BH8701CL', 'HH3296ZU', 'HH1477XI',
               'BH7181HC', 'HH8586XZ', 'AI4713UM', 'HH7004VD', 'HH1870YL', 'BH8685FA', 'HH0366RH', 'AI2619VK',
               'CA0716YN', 'HH3949DF', 'CA6576XD', 'HH4775VT', 'CA6185EC', 'BH7583RG', 'HH4056GM', 'HH0910EX',
               'HH1234FS', 'HH9555HO', 'HH6404BO', 'CA0491XQ', 'AI4375UJ', 'AI4544XP', 'HH9934AE', 'CA6967QC',
               'BH6055GX', 'CA1078RJ', 'BH5484QP', 'BH0239HO', 'AI1887EI', 'CA2434ZR', 'AI5168QP', 'BH1537OZ',
               'CA4836UF', 'HH6192XL', 'AI7844LN', 'AI5065FJ', 'CA5273JS', 'BH1816ZF', 'AI3474UV', 'CA6100FM',
               'HH4607TE', 'HH9897KJ', 'AI0065JQ', 'AI8686DD', 'CA6479NQ', 'BH9693BR', 'HH0384HY', 'CA6558PZ',
               'BH8770OB', 'HH2772UM', 'CA7711DW', 'HH1431XO', 'AI7798TY', 'AI5479BQ', 'AI9194VA', 'AI4987SZ',
               'CA3596OQ', 'HH3179YB', 'HH9257TB', 'CA1283JM', 'CA4407NW', 'CA3406IX', 'HH3382OK', 'HH1532AF',
               'CA3542AH', 'AI4410MR', 'CA0854QZ', 'CA4448WO', 'CA8594GE', 'CA2002MG', 'BH1595SC', 'CA0828HE',
               'HH1172QR', 'HH6589NP', 'AI8079KI', 'HH0390XU', 'AI3212IT', 'BH6446GU', 'HH8009KT', 'AI8962RC',
               'AI5838YR', 'CA0050XE', 'BH6084RF', 'HH9395QN', 'AI5035ET', 'CA9150WC', 'HH0989TP', 'CA0260YS',
               'CA8821BK', 'AI8692KN', 'HH2874PV', 'BH7128UV', 'HH8047MO', 'CA2084KK', 'AI7508JT', 'BH1391WD',
               'AI5324LK', 'HH1511HA', 'HH8408CA', 'AI8090RI', 'HH2020VT', 'BH2591VY', 'HH7563KS', 'CA5289XN',
               'BH2532MR', 'CA1757VV', 'AI9668GU', 'HH8200RW', 'AI0295LI', 'AI6821VK', 'CA7461LL', 'BH2504RW',
               'AI1170JA', 'HH8792IV', 'CA1773PV', 'HH1924CH', 'BH6199UT', 'BH7815II', 'AI1858XK', 'AI3351MX',
               'HH1580QX', 'HH5735MH', 'AI1434BG', 'CA4496GO', 'AI3911CP', 'BH1565XV', 'HH6575MD', 'CA8832ID',
               'BH4691NS', 'HH4624ZU', 'AI8105YW', 'BH5203BF', 'AI1279KS', 'CA4107BY', 'AI5144CE', 'CA0379AN',
               'HH7221AN', 'BH1639AS', 'CA2335MT', 'BH7500CG', 'HH3455AL', 'BH0427GT', 'CA3555IC', 'HH1117WE',
               'BH5127JE', 'HH6890GI', 'HH4244FJ', 'HH1710QZ', 'CA8475AT', 'CA3297JN', 'CA3886HU', 'AI1224UU',
               'BH4379IW', 'CA8535GZ', 'AI2181MC', 'CA4848HA', 'HH9958BX', 'BH1517QM', 'AI6115SK', 'HH3979UN',
               'HH4034JT', 'AI9809PQ', 'AI5473LE', 'AI6534XO', 'BH8595KO', 'AI6230NM', 'CA3011XM', 'AI4108DK',
               'HH7313EV', 'HH9374NB', 'HH7537AS', 'BH0958NC', 'HH5133PK', 'AI9808HA', 'BH6183VY', 'HH6047WU',
               'CA2791IP', 'CA0902KT', 'AI7750BF', 'CA9217PC', 'HH1008KM', 'AI1930RO', 'BH6515VR', 'AI5838YR',
               'AI1457RC', 'BH8578WX', 'CA0523AN', 'AI9443FT', 'AI2868HE', 'HH6364SI', 'HH1771YW', 'HH8098EA',
               'CA3387AM', 'CA6832GS', 'CA2203BF', 'AI1602AK', 'BH8742YE', 'CA5849KA', 'BH3595QT', 'CA8684UW',
               'AI2122TC', 'AI9480YM', 'AI6844MQ', 'BH1076US', 'HH8349GH', 'HH7092AG', 'BH1267RQ', 'AI9592EZ',
               'BH4830UW', 'AI6895OT', 'AI2802ID', 'HH7189JX', 'CA1677UA', 'AI3899LK', 'AI2702NU', 'HH8103ER',
               'HH6252NO', 'CA2551CK', 'CA1089QW', 'CA2392OX', 'HH6018PM', 'CA3456FP', 'AI7352UM', 'AI7178ZH',
               'AI3312NI', 'CA9032UP', 'CA9006UL', 'BH1493GB', 'BH7962QH', 'BH3343PB', 'BH4235UN', 'AI0146LO',
               'BH0291QQ', 'CA6120HH', 'BH1755CK', 'BH1304NG', 'CA0344OA', 'BH2279BN', 'CA1126CD', 'AI1550YW',
               'BH0800IM', 'BH3240AK', 'BH3359HE', 'HH5326MH', 'BH9582TT', 'HH9227HA', 'HH9823AO', 'BH6135HE',
               'BH3454ID', 'HH5788EA', 'HH4310TF', 'HH2631PJ', 'CA2819OV', 'CA5301LD', 'CA0054TU', 'AI6911OT',
               'BH9028NO', 'BH7997VD', 'AI0910UV', 'CA0184WV', 'CA1010ZR', 'BH2690WY', 'BH6131GB', 'AI9805RD',
               'BH4643VE', 'CA5262FP', 'CA0032RT', 'HH2731XE', 'BH5970GQ', 'CA0600RO', 'CA5417SF', 'AI5185WO',
               'CA3467BE', 'HH4075LP', 'HH9216EE', 'HH6182BL', 'HH0541GM', 'HH2501LW', 'BH9816VV', 'HH5099GQ',
               'AI7408EU', 'BH4222DX', 'BH6861JM', 'CA4324IS', 'BH7403TT', 'BH3459LZ', 'BH4244ID', 'AI7336YS',
               'BH0903US', 'AI8438CV', 'AI6342OW', 'AI6981VY', 'CA8707AK', 'BH9243UA', 'HH3449AV', 'BH9418NS',
               'BH6394UO', 'BH1787SW', 'HH4684WF', 'AI1539HV', 'HH7498GG', 'CA2283UQ', 'BH4063PR', 'CA6683SI',
               'AI4249LK', 'HH6172WA', 'AI0032QI', 'CA0370ZU', 'CA7635WM', 'CA9302KX', 'CA9695SU', 'AI1692XJ',
               'CA2593QI', 'AI9342FB', 'CA9763ZR', 'BH9001CY', 'HH3231TK', 'CA2633QH', 'BH7388BK', 'CA9999AU',
               'CA5633HZ', 'HH8883XG', 'CA6737HF', 'HH5510FG', 'AI9982SI', 'BH9362OX', 'CA3775XA', 'AI1942IA',
               'AI2156CW', 'CA5212ES', 'BH2542HT', 'CA4640PP', 'BH5931EW', 'CA0844TY', 'CA6694EX', 'BH4053PH',
               'HH0965ZL', 'HH1909XZ', 'AI1368DE', 'AI4300UU', 'CA1449SC', 'HH7097ZH', 'BH3044HJ', 'AI4460GE',
               'CA4431SI', 'HH6453ZG', 'CA3480YI', 'AI3020PB', 'BH0008KK', 'HH9482LY', 'CA1227OW', 'CA3931XQ',
               'HH0200HE', 'CA0044VF', 'HH2188DO', 'HH3420UK', 'HH4469SG', 'BH3906HM', 'HH9601US', 'HH7603BV',
               'AI6337LJ', 'BH9973DJ', 'AI0389DC', 'AI3931TH', 'HH9269VV', 'AI7086OE', 'HH0983UX', 'BH5121FD',
               'CA4120CT', 'CA3742IE', 'CA8825MH', 'BH2881MU', 'CA1501UF', 'AI5465RY', 'BH8092ZU', 'CA5603TS',
               'AI6378YH', 'CA2742HE', 'CA4250MG', 'BH8024NU', 'AI9021LL', 'CA9343BS', 'HH7291JG', 'CA3740MS',
               'AI2289GO', 'BH7329ZV', 'HH8242TZ', 'AI9394DD', 'BH7489UI', 'BH9392LS', 'AI5509FR', 'BH6812PB',
               'CA1008ZM', 'CA8771TK', 'CA5899DX', 'BH8107QJ', 'CA0253SO', 'AI5084LF', 'AI1669DV', 'BH6640IY',
               'BH7312QT', 'BH5116SS', 'AI4967PE', 'BH4096LZ', 'CA3532IB', 'AI1041ER', 'CA3259XB', 'HH1848DD',
               'CA8679DS', 'HH0736MI', 'CA4245JG', 'AI6531OF', 'AI2767LJ', 'CA4625LO', 'BH4868GG', 'CA3278CW',
               'BH8407KS', 'HH9394EJ', 'AI9440LI', 'BH5857IW', 'CA6365HW', 'CA1606OJ', 'CA4627CG', 'CA9798BG',
               'AI5219RH', 'BH7940VS', 'BH6596UU', 'BH9942IX', 'CA6614CF', 'BH6027HX', 'BH7419YV', 'BH2259JL',
               'HH8919CP', 'CA2374WZ', 'AI4790GF', 'AI0203AA', 'CA1415VE', 'CA2187RZ', 'AI1988IS', 'AI6587TU',
               'BH4122UO', 'AI5150SJ', 'BH3143OQ', 'HH7629FF', 'AI4337BB', 'AI4611BD', 'AI6398BQ', 'HH1789WY',
               'BH8997CL', 'HH2817NA', 'HH1700EI', 'HH1527WZ', 'AI9398TP', 'HH0792PD', 'CA0281LG', 'BH9209YY',
               'AI7453WB', 'HH7030IC', 'HH8046BN', 'AI6783OP', 'HH0151SV', 'AI5535VY', 'AI3313ON', 'AI5701WH',
               'CA5050SB', 'HH9269VV', 'AI0045RJ', 'HH8609RB']
new_plate_list = set(plates_list)
print("Amount of plates in the list is :", len(new_plate_list))
your_number = functions_dz.plate()
if your_number in plates_list:
    print("Congrats you're in the list!!")
else:
    print("Sorry, bro")
