


//var csv to json file with headers


function csvJSON(){
  var sheet = SpreadsheetApp.getActiveSheet();
   var data = sheet.getDataRange().getValues();
  var results = [];
  var phenopakkets = [];

  for (var i = 2; i < data.length; i++) {

    
    //cohortjson
    cohortjson={};
    cohortjson[data[0][2]]=data[i][2];
      
    
    
    cohortObject={};
    cohortObject["cohort"]=cohortjson
	
        results.push(cohortObject);

    
        //Indivisualjson
    Indivisualjson={};
    Indivisualjson[data[0][0]]=data[i][0];
    Indivisualjson[data[0][5]]=data[i][5];	
    Indivisualobject={};
    Indivisualobject["Individual"]=Indivisualjson;
	
      phenopakkets.push(Indivisualobject);

	//Samplejson
    Samplejson={};
    Samplejson[data[0][1]]=data[i][1];
    Samplejson[data[0][6]]=data[i][6];
    Samplejson[data[0][8]]=data[i][8];
    Samplejson[data[0][21]]=data[i][21];
	
    Sampleobject={};
    Sampleobject["Biosample"]=Samplejson;
	
        phenopakkets.push(Sampleobject);
	
      	//diseasejson
    Diseasejson={};
    Diseasejson[data[0][4]]=data[i][4];
    Diseasejson[data[0][7]]=data[i][7];
      
    
    
    Diseaseobject={};
    Diseaseobject["Disease"]=Diseasejson
	
        phenopakkets.push(Diseaseobject);

	
      //phenotypicfeatures
    Phenotypicfeaturesjson={};
      if (i ==2)
      Phenotypicfeaturesjson["type"]=data[i][10];
      else
      Phenotypicfeaturesjson["severity"]=data[i][10];
      
      PhenotypicFeatureobject={};
      PhenotypicFeatureobject["PhenotypicFeature"]=Phenotypicfeaturesjson;
	
        phenopakkets.push(PhenotypicFeatureobject);
    
    
    PhenopacketObject={};
    PhenopacketObject["Phenopakket"]=phenopakkets;
	 
    results.push(PhenopacketObject)
    

  }

  
  var jsonString = JSON.stringify(results); //JavaScript object
  console.log(jsonString); //JSON
  
  return jsonString;
}


