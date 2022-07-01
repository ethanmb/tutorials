/* * * * * * * * * * * * * * * * * * * *  * * * * * * * */
/*                                                      */
/*  Program:  Foood2Fork SPA                            */
/*  Authors: Ethan Brown 101031125, Nima Dadar 100898748*/
/*  Date:     NOV-22-2017                               */
/*                                                      */
/* * * * * * * * * * * * * * * * * * * * *  * * * * * * */

const express = require('express');
const requestM = require('request');
const bodyParser = require('body-parser');
const application = express();
const API_KEY = "919e61eab74a7bad03d31d307ec5dd49";
const logger = require('morgan');

application.set('port', process.env.PORT || 3000);
application.use(bodyParser.json());
application.use(bodyParser.urlencoded({ extended: true }));
application.use( logger('dev'));


function getRecipes(ingredient, res)
{
	var URL = 'http://food2fork.com/api/search?key=' + API_KEY
	if (ingredient != null)
		URL += '&q=' + ingredient
	requestM(URL, (err, resp, data) => {
		if (err) { 
			console.log(err);
		}else {
			sendResponse(data, res);
		}
	});
}

function sendResponse(apiData, res)
{	
	var htmlPage = '<html><head><title>Ethan Brown, Nima Dadar</title>' +
	'</head><body>' +
    '<form method="post"> <div class="center">' +
    'Enter an Ingredient: <input name="ingredient" style="height: 30px;">' +
    '<input type="submit" value="Submit">' +
    '</div></form>';
	//if there is data, create a page
	if (apiData)
	{
		//parse data coming in, so it is usable
		apiData = JSON.parse(apiData);
		//limit the amount of recipes shown
		if (apiData.count > 20)
			//splitting recipes
			apiData.recipes = apiData.recipes.splice(0, 20);
		htmlPage += '<table table-layout: fixed;"><tr>';
		for (var i = 0; i < apiData.recipes.length; i++)
		{
			//adding images and links to html page
			htmlPage += '<td class="element"><a href=' + apiData.recipes[i].f2f_url + ' target="_blank">' + 
			'<img src="' + apiData.recipes[i].image_url + '" alt="Girl in a jacket" width="400" height="250"><br>' + apiData.recipes[i].title + '</div></a></td>';
			//creates a new row every 5 recipes
			if ((i+1)%5 == 0 && i != 0)
				htmlPage += '</tr><tr>';
		}
		htmlPage += '</tr></table>';
	}
	htmlPage += '</body><html>';
	res.send(htmlPage);
}

application.get('/recipes', function(req, res){
	getRecipes(req.query.ingredient, res);
});

application.post('/recipes', function(req, res) {
	getRecipes(req.body.ingredient, res);
});

application.listen(application.get('port'), function(){
	console.log("Server started at  http://127.0.0.1:3000 PORT:" + application.get('port') + ". Ctrl-C to end.");
});