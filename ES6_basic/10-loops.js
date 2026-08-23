export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;

  // eslint-disable-next-line space-in-parens
  for ( const value of array) {
    // eslint-disable-next-line no-param-reassign
    array[idx] = appendString + value;
    idx += 1;
  }

  return array;
}
