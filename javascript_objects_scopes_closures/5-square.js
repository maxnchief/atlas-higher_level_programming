#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

// 5-square.js

class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }
}

module.exports = Square;