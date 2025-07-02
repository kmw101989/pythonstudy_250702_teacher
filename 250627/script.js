const num01 = 10;
const num02 = 20;

const multi = (num01, num02) => {
  return () => {};
};

multi()();

const fin = multi(num01, num02);

console.log(fin);
