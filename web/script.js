function factorial(n) {
  if ((n == 0)) {
    return 1;
  } else {
    return (n * factorial((n - 1)));
  }
}
function fibonacci(n) {
  if ((n == 0)) {
    return 0;
  } else {
    if ((n == 1)) {
      return 1;
    } else {
      return (fibonacci((n - 1)) + fibonacci((n - 2)));
    }
  }
}
console.log('Factorial of 5 is', factorial(5));
console.log('10th Fibonacci number is', fibonacci(10));
