function onOpen() {
  SpreadsheetApp.getUi() // Or DocumentApp or SlidesApp or FormApp.
      .createMenu('Phenopackets Menu')
      .addItem('Generate JSON', 'generateJSON')
      .addToUi();
}

function generateJSON() {
  
  var output = HtmlService.createHtmlOutput('<b>Phenopacket JSON</b>');
output.append('<p>');
  var jsonString = csvJSON();
  console.info(jsonString);
  output.append(jsonString);
  output.append('</p>');
Logger.log(output.getContent());
  
  //var html = HtmlService.createHtmlOutputFromFile('Page')
   //   .setTitle('My custom sidebar')
   //   .setWidth(300);
  SpreadsheetApp.getUi() // Or DocumentApp or SlidesApp or FormApp.
      .showSidebar(output);
}
