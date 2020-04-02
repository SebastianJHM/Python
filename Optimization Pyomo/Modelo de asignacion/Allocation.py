import pyomo.environ as pyo
from pyomo.opt import SolverFactory

## ----------------------- MODELO -------------------------------
opt = SolverFactory('cplex', executable="C:\\Program Files\\IBM\\ILOG\\CPLEX_Studio1210\\cplex\\bin\\x64_win64\\cplex")
#opt = SolverFactory('glpk')
model = pyo.AbstractModel()

## --------------------- CONJUNTOS ----------------------------
model.REF = pyo.Set()
model.RACKS = pyo.Set()

## ---------------------- PARÁMETROS ----------------------------
model.AnchoCaja = pyo.Param( model.REF )
model.TipoDist = pyo.Param( model.REF )
model.Espacios = pyo.Param( model.REF, mutable=True )
model.TipoRack = pyo.Param( model.RACKS )
model.Pared = pyo.Param( model.RACKS )
model.Utilizacion = pyo.Param( model.RACKS )

model.Demanda  = pyo.Param( model.REF )
model.Frecuencia  = pyo.Param( model.REF )
model.Costo = pyo.Param( model.RACKS )

## ---------------------- VARIABLES ----------------------------
model.x = pyo.Var( model.REF, model.RACKS, domain = pyo.Binary )
model.y = pyo.Var( model.RACKS, domain = pyo.Binary )

## ---------------------- FUNCIÓN OBJETIVO ----------------------------
def ObjFunc( model ):
    return sum(model.Demanda[ref]*model.Frecuencia[ref]*model.Costo[rack]*model.x[ref,rack] for ref in model.REF for rack in model.RACKS )
#fed
model.FO = pyo.Objective( rule = ObjFunc )

## ---------------------- RESTRICCIONES ----------------------------
def r1( model, ref ):
    return sum( model.x[ref,rack] for rack in model.RACKS ) == 1
#fed
model.r1 = pyo.Constraint( model.REF, rule = r1 )

def r2( model, rack ):
    return sum( model.AnchoCaja[ref]*model.x[ref,rack] for ref in model.REF ) <= 250*(1-model.y[rack]) + 750*(model.y[rack])
#fed
model.r2 = pyo.Constraint( model.RACKS, rule = r2)

def r3( model, ref, rack):
    return model.x[ref,rack] <= (model.y[rack]*model.TipoDist[ref]) + ((1-model.y[rack])*(1-model.TipoDist[ref]))
#fed
model.r3 = pyo.Constraint( model.REF, model.RACKS, rule = r3 )

def r6( model, ref, rack ):
    return model.Espacios[ref]*model.x[ref,rack] <= model.TipoRack[rack]
#fed
model.r6 = pyo.Constraint( model.REF, model.RACKS, rule = r6 )

def r8( model, rack ):
    return model.y[rack] <= 1 - model.Pared[rack]
#def
model.r8  = pyo.Constraint( model.RACKS, rule = r8 )
 
def r9( model, ref, rack ):
    return model.x[ref,rack] <= model.Utilizacion[rack]
#def
model.r9 = pyo.Constraint( model.REF, model.RACKS, rule = r9 )


## ============= Create a model instance and optimize =================
instance = model.create_instance('Data_Allocation_1.dat')
opt.options['timelimit'] = 40
results = opt.solve(instance, tee = False)
#instance.display()
## ====================================================================

def print_result_console( instance ):
    
    
    Racks_Real = ["P1",	"P2",	"P3",	"P4",	"P5",	"P6",	"P7",	"P8",	"P9",	"P10",	"P11",	"P12",	"P13",	"P14",	"P15",	"A1",	"A2",	"A3",	"A4",	"A5",	"A6",	"A7",	"A8",	"A9",	"A10",	"A11",	"A12",	"A13",	"A14",	"A15",	"C1",	"C2",	"C3",	"C4",	"C5",	"C6",	"C7",	"C8",	"C9",	"C10",	"C11",	"C12",	"C13",	"C14",	"C15",	"D1",	"D2",	"D3",	"D4",	"D5",	"D6",	"D7",	"D8",	"D9",	"D10",	"D11",	"D12",	"D13",	"D14",	"D15",	"G1",	"G2",	"G3",	"G4",	"G5",	"G6",	"G7",	"G8",	"G9",	"G10",	"G11",	"G12",	"G13",	"G14",	"G15",	"H1",	"H2",	"H3",	"H4",	"H5",	"H6",	"H7",	"H8",	"H9",	"H10",	"H11",	"H12",	"H13",	"H14",	"H15",	"K1",	"K2",	"K3",	"K4",	"K5",	"K6",	"K7",	"K8",	"K9",	"K10",	"K11",	"K12",	"K13",	"K14",	"K15",	"K16",	"K17",	"K18"]
    Refs_Real = ["5096",	"1418",	"1425",	"0152",	"1388",	"1401",	"1647",	"1784",	"3566",	"5102",	"1814",	"3610",	"3740",	"5027",	"5133",	"5232",	"0022",	"0121",	"1500",	"1609",	"1722",	"5164",	"5188",	"0787",	"1487",	"1548",	"1579",	"1654",	"5072",	"5225",	"0688",	"1678",	"1807",	"3580",	"3719",	"5003",	"5119",	"1432",	"1456",	"1685",	"4990",	"1616",	"1845",	"1463",	"1562",	"1470",	"1494",	"1517",	"1630",	"1708",	"1791",	"5126",	"1586",	"1623",	"1661",	"1692",	"1753",	"3573",	"5058",	"1593",	"1715",	"1999",	"3597",	"3603",	"5171",	"5201",	"0435",	"0442",	"2057",	"2255",	"2262",	"3467",	"4013",	"4020",	"4044",	"4051",	"4082",	"4105",	"4112",	"8509",	"8523",	"8554",	"8585",	"8592",	"8639",	"8660",	"8684",	"8691",	"8707",	"8721",	"8738",	"8745",	"8769",	"8776",	"2170",	"8431",	"8455",	"8462",	"8479",	"8486",	"8493",	"8516",	"8530",	"8547",	"8561",	"8578",	"8608",	"8615",	"8622",	"8646",	"8653",	"8677",	"8714",	"8752",	"8790",	"8806",	"1333",	"1395",	"1555",	"2194",	"3696",	"4198",	"0671",	"1357",	"1821",	"1838",	"4846",	"4853",	"4860",	"4877",	"4976",	"4983",	"5010",	"5065",	"5157",	"5195",	"1449",	"1777",	"3634",	"3702",	"5034",	"5041",	"5089",	"0039",	"0046",	"0053",	"0060",	"0459",	"0527",	"0534",	"1302",	"1524",	"1913",	"3474",	"4235",	"4242",	"4259",	"4266",	"6307",	"1968",	"3917",	"4273",	"4280",	"4297",	"4303",	"0145",	"1340",	"3962",	"3979",	"4150",	"4341",	"4358",	"0220",	"3900",	"4327",	"4334",	"2156",	"4167",	"4785",	"7007",	"7014",	"1272",	"1289",	"3672",	"3849",	"4006",	"4174",	"4181",	"4747",	"4754",	"4761",	"4778",	"6161",	"6987",	"9469",	"0961",	"2538",	"3887",	"3924",	"4457",	"0640",	"6550",	"3290",	"3306",	"3313",	"3320",	"3337",	"7519",	"7526",	"7533",	"7540",	"8134",	"0183",	"0206",	"0893",	"1531",	"1739",	"1746",	"1760",	"2569",	"2576",	"0169",	"1920",	"2378",	"2514",	"2545",	"2552",	"2644",	"3542",	"3559",	"3801",	"3993",	"4143",	"0503",	"0510",	"1197",	"2019",	"3252",	"3450",	"3856",	"3863",	"4136",	"6284",	"0480",	"0954",	"4396",	"4464",	"4471",	"4501",	"4525",	"4532",	"4624",	"4648",	"0596",	"0619",	"0497",	"2521",	"0558",	"0565",	"0572",	"0589",	"0602",	"0855",	"2279",	"2286",	"3269",	"4372",	"6314",	"6321",	"6956",	"6963",	"6970",	"6994",	"7748",	"7755",	"7762",	"7779",	"7786",	"7793",	"7809",	"7892",	"7908",	"7915",	"7922",	"7939",	"7946",	"7953",	"6628",	"6635",	"6642",	"6659",	"6666",	"6673",	"6680",	"6697",	"6703",	"2071",	"2101",	"6611",	"7564",	"7571",	"7588",	"7632",	"7649",	"7663",	"7670",	"7687",	"4389",	"6062",	"6079",	"6130",	"6185",	"6253",	"6444",	"6505",	"6604",	"6918",	"9230",	"9247",	"9254",	"9261",	"0190",	"2149",	"2187",	"3818",	"4402",	"4419",	"4426",	"4433",	"4440",	"4488",	"4495",	"4518",	"4549",	"4556",	"4563",	"4570",	"4587",	"4594",	"4617",	"4631",	"4655",	"4662",	"4679",	"4686",	"4693",	"4730",	"2668",	"3627",	"4075",	"5263",	"5270",	"5294",	"5331",	"5386",	"5393",	"5461",	"5560",	"5577",	"5645",	"5720",	"5768",	"5881",	"5959",	"5966",	"6857",	"6864",	"6888",	"HB026",	"4037",	"4211",	"5256",	"5300",	"5355",	"5409",	"5508",	"5522",	"5553",	"5591",	"5614",	"5652",	"5683",	"5706",	"5713",	"5737",	"5775",	"5782",	"5805",	"5843",	"5850",	"5867",	"5874",	"5898",	"5935",	"6895",	"2675",	"3948",	"5324",	"5348",	"5362",	"5379",	"5430",	"5447",	"5454",	"5478",	"5485",	"5492",	"5515",	"5546",	"5607",	"5621",	"5669",	"5676",	"5690",	"5744",	"5751",	"5799",	"5812",	"5836",	"5928",	"5942",	"6871",	"7120",	"7694",	"7861",	"8073",	"8103",	"0541",	"0800",	"0862",	"0879",	"0886",	"0930",	"2064",	"3245",	"7854",	"HA014",	"HA032",	"HB016",	"M007",	"M008",	"0978",	"0985",	"0992",	"1005",	"1012",	"1029",	"1036",	"1043",	"6833",	"9209",	"9216",	"9223",	"9278",	"9285",	"9292",	"HB021",	"HB022",	"HB023",	"1104",	"1111",	"1296",	"1319",	"2606",	"0664",	"0701",	"2385",	"2583",	"2620",	"3481",	"6338",	"6352",	"6383",	"6413",	"6567",	"6574",	"6598",	"HB032",	"2408",	"2415",	"2491",	"3283",	"3498",	"4914",	"6086",	"6260",	"6345",	"6369",	"6376",	"6390",	"6406",	"6420",	"6451",	"6468",	"6475",	"6482",	"6499",	"6512",	"6529",	"3689",	"4228",	"4310",	"4907",	"6093",	"6109",	"6116",	"6123",	"6147",	"6192",	"6208",	"6215",	"6222",	"6239",	"6246",	"6277",	"HB025",	"HB027",	"HB028",	"6024",	"6031",	"6048",	"6055",	"2460",	"6727",	"6734",	"6758",	"1241",	"6772",	"6819",	"6796",	"8035",	"8059",	"6710",	"6741",	"6765",	"6789",	"6802",	"6826",	"5980",	"5997",	"6000",	"6017"]
    
    print("\n\n")
    print("SOLUCIÓN DEL EJERCICIO")
    print("--------------------------")
    print("\n")
    print("Función Objetivo: ",pyo.value(instance.FO))
    print("\n")
    for rack in instance.RACKS:
        print("===== ", Racks_Real[rack-1],"; H: ", instance.y[rack].value ,"=====")
        for ref in instance.REF:
            if ( instance.x[ref,rack] == 1 ):
                print("Ref: ", Refs_Real[ref-1],"; D*F = ",instance.Demanda[ref]*instance.Frecuencia[ref])
            #fi
        #rof
    #rof
    print("Función Objetivo: ",pyo.value(instance.FO))
    
#    print("\n\n")
#    print("SOLUCIÓN DEL EJERCICIO")
#    print("--------------------------")
#    print("\n")
#    print("Función Objetivo: ",pyo.value(instance.FO))
#    print("\n")
#    for ref in instance.REF:
#        for rack in instance.RACKS:
#            if ( instance.x[ref,rack] == 1 ):
#                print("La referencia ", ref ," en el rack", Racks_Real[rack-1])
#            #fi
#        #rof
#    #rof
#    print("Función Objetivo: ",pyo.value(instance.FO))
    
    print("\n\n")
    print("SOLUCIÓN DEL EJERCICIO")
    print("--------------------------")
    print("\n")
    print("Función Objetivo: ",pyo.value(instance.FO))
    print("\n")
    for ref in instance.REF:
        for rack in instance.RACKS:
            if ( instance.x[ref,rack] == 1 ):
                print("La referencia ", ref ," en el rack", rack)
            #fi
        #rof
    #rof
    print("Función Objetivo: ",pyo.value(instance.FO))
#fed

print_result_console( instance )