#!/usr/bin/node
// This script prints all characters of a Star Wars movie

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(url, async (err, response, body) => {
  if (err) {
    console.log(err);
  }
  for (const characterId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(characterId, (err, response, body) => {
        if (err) {
          reject(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
