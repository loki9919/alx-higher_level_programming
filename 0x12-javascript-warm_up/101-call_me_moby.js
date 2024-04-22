#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
    for (var i = 0 ; i < x; i++)
    {
        theFunction();
    }
}