##Main

#3D test:
from test_3D import hello, function3D, function3D_args
from analysis_module import *
from math_module import *

import sys, getopt
import argparse

def func_do_script(arg,arg2):
    """ This function is the main funciton, basically generates all the scripts:
    ""  take the metrics, read the json, generates list of this json put in a dictionary
    "   then it trainnes a svm and then classify the information using this module and finally gives an output with the classification
    """
    #Generates an analysis, which is defined in analysis_module
    analysis = trace_analysis(arg,1,'N')
    
    #Do the same but for h - wait-blocked: a for duration
    #hello()
    #Function for 3D modules: function3D_args([1,2,3,4,5,6,7,8,9,10],[5,6,7,3,3,5,7,9,11,8],[2,3,3,3,5,7,9,11,9,10])

    #Define Metrics:
    metric = ['a','b','g']
    #Define an dictionary:
    dictionary = analysis.do_lists_full()

    #Print the list of a metric for this specific dictionary:
    analysis.print_function(dictionary,'g')

    #Do 3D graphs:
    #function3D_args(dictionary['a'],dictionary['b'],dictionary['e'],metric)
    #calc_square_sum(dictionary['a'],dictionary['b'],dictionary['e'])

    print("Lista duration --")
    metric = 'a' #a corresponds in trace compare to duration
    lista = analysis.do_lists(metric)
    print(len(lista))

    #svm_ovo()

    #Do the graph:
    analysis.do_graph(lista,"bar")

    #Do histogram:
    histogram = analysis.do_histogram(lista)

    #Do an array:
    array = analysis.create_array(histogram)
    print(array)

    #create an array of [metric1, metric2, timestamp]
    print("--- Example ---")
    example = analysis.merge_metrics(dictionary['a'],dictionary['h'],[])#dictionary['b'],dictionary['a'],dictionary['g'])
    print(example)

    #data:
    #example = ['a','h']
    #array is a histogram

    #Plot the graph:
    analysis.print_graph(example)

    #SVM:
    a=[19,0]
    b=[21,0]

    #new_list = SVM_2(a,b,example,metric) #classify in 3 groups
    #svm_ovo()

    #Defining tranning groups:
    list_x = [[0,0],[50,0],[150,0],[6,6],[10,10],[0,5],[350,0],[250,0],[200,0],[340,10],[350,5],[325,7]]
    list_y = ['A','A','A','B','B','B','C','C','C','D','D','D']
    #svm_ovo_applied(lista_x,lista_y,[1,0]):
    ans = analysis.takes_list_gives_svm_ovo_result(list_x, list_y, example) #[[1,2,'b'],[2,4,'b']]
    #plot:
    #analysis.plot_point_color(ans)
    #separate the groups in a dictionary:
    dic_groups = analysis.build_groups(ans)

    print("Group A")
    print(dic_groups['A'])

    print("Group B")
    print(dic_groups['B'])

    print("Group C")
    print(dic_groups['C'])

    print("Group D")
    print(dic_groups['D'])

    #csv:
    #analysis.write_csv(arg2,dic_groups)
    analysis.write_groups_csv(arg2,dic_groups,'N')#n stands for not print group labels:
    
    return dic_groups
    #new_list = SVM(a,b,array,metric)
    #Show:
    #print("Optimal group")
    #print(new_list['OPT'])

    #print("Not optimal group:")
    #print(new_list['NOPT'])

    #Show all metrics:
    #all_metrics = do_list_full()
    #print(len(all_metrics))

    #Function that grabs a list of a specific metric:
    #list_result_mopt = search_list(all_metrics, new_list['MOPT'],metric)
    #print("Info about the Opt list")
    #print(list_result_mopt)
     
    #Function that grabs a list of a specific metric:
    #list_result_opt = search_list(all_metrics, new_list['OPT'],metric)
    #print("Info about the Opt list")
    #print(list_result_opt)

    #Shows list_result which is the list of the metric NOPT
    #list_result_nopt = search_list(all_metrics, new_list['NOPT'],metric)
    #print("Info about the nopt list")
    #print(list_result_nopt)

    # ----Second Analysis:
    #Take a list of a specific metric:
    #0679 01013429-8
    #166 963 538-44

    #metric = ['h','a','b']
    #list_dimension_x = search_list_in_list(list_result_opt,metric[0])
    #len(list_dimension_x)

    #list_dimension_y = search_list_in_list(list_result_opt,metric[1])
    #len(list_dimension_y)

    #list_dimension_z = search_list_in_list(list_result_opt,metric[2])
    #len(list_dimension_z)
    #Plot
    #function3D_args(list_dimension_x,list_dimension_y,list_dimension_z,metric)

    #Does a mean of a specific metric:
    #wait-blocked
    #mean_metric(list_result_opt,metric[0])
    #mean_metric(list_result_nopt,metric[0])
    #duration
    #mean_metric(list_result_opt,metric[1])
    #mean_metric(list_result_nopt,metric[1])
    #timestamp
    #mean_metric(list_result_opt,metric[2])
    #mean_metric(list_result_nopt,metric[2])

    #samples:
    #list_samples(list_result_opt)

#De test using input output:
def do_test(inputFile, outputFile):
    "This function calls the complete analysis using input and output file"
    print("Group A")
    if len(outputFile) and len(outputFile)>0: 
        ans = func_do_script(inputFile,outputFile)# json and csv
        
#Default argument:
def do_test():
    "This function calls the complete analysis using input and output file"
    print("Group A")
    ans = func_do_script('data/open1000.json',"data/test.csv")# json and csv
        
def metrics_generator(inputFile, outputFile):
    print ('This is the metric generator from json to csv')
    print (inputFile)

    analysis = trace_analysis(inputFile,1,'N') #inputfile, identification and graph mode (N - off, Y - on)
    #Define Metrics that will be in the CSV:
    metric = ['a','b','g']
    #Define an dictionary:
    dictionary = analysis.do_lists_full()
    
    #Call the write to outputfile:
    analysis.write_groups_in_csv(outputFile,dictionary)
    
def main(argv):
    print argv
    if (argv[0] == '-h'):
        print 'This program is a module to analyse TRACE COMPARE (json) files'
        print 'Enter the input and output name'
    if (argv[0] == '-v'):
        print 'This program is a module to analyse TRACE COMPARE (json) files'
    if (argv[0] == '-m'):
          print 'This will convert a json in csv file'
          if len(argv)>1:
              metrics_generator(argv[1],argv[2])
          else:
              print 'Enter input and output files'
    if (argv[0] == '-a'):
          print 'This will analyse a json generating a output'
          if len(argv)>1:
              do_test(argv[1], argv[2])
          else:
              do_test()
          
        
if __name__ == "__main__":
   main(sys.argv[1:])



