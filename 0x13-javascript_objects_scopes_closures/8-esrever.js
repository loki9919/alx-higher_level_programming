exports.esrever = function (list) {
  const reveselist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reveselist.push(list[i]);
  }
  return reveselist;
};
