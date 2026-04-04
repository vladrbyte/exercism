//
// This is only a SKELETON file for the 'Collatz Conjecture' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const steps = (n, count=0) => {
  if(n>0){
    while(n>1){
      count++
      n%2==0 ? n/=2 : n=n*3+1 
    }
    return count
  }
  throw new Error('Only positive numbers are allowed');
};
