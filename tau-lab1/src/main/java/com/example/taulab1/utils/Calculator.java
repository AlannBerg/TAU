package com.example.taulab1.utils;

import static java.util.Objects.isNull;

public class Calculator {

  public Integer add(Integer a, Integer b) {
    if (isNull(a) || isNull(b)) {
      throw new RuntimeException("Can not add null value");
    }
    return a + b;
  }

  public Integer subtract(Integer a, Integer b) {
    if (isNull(a) || isNull(b)) {
      throw new RuntimeException("Can not subtract null value");
    }
    return a - b;
  }

  public Integer multiply(Integer a, Integer b) {
    if (isNull(a) || isNull(b)) {
      throw new RuntimeException("Can not multiply null value");
    }
    return a * b;
  }

  public Integer divide(Integer a, Integer b) {
    if (isNull(a) || isNull(b)) {
      throw new RuntimeException("Can not multiply null value");
    }
    if(b == 0){
      throw new RuntimeException("Can not divide by 0");
    }
    return a / b;
  }
}
