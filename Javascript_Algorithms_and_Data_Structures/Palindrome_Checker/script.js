function palindrome(str) {
    let adjustStr =/[^\w]|_/g;
    let normalStr = str.replace(adjustStr, '').toLowerCase();
    let reversedStr = normalStr.split('').reverse().join('');
    if (normalStr === reversedStr) {
      return true
    } else {
      return false
    }
  }
  
  palindrome("eye");