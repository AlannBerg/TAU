package com.example.taulab1.utils;

import org.junit.Assert;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class CalculatorTest {

  Calculator calculator = new Calculator();

  @Test
  @DisplayName("Should add numbers")
  void addIntegers() {
    Integer a = 5;
    Integer b = 5;
    int result = calculator.add(a, b);
    Assert.assertEquals(result, 10);
  }

  @Test
  @DisplayName("Should subtract numbers")
  void subtractIntegers() {
    Integer a = 5;
    Integer b = 5;
    int result = calculator.subtract(a, b);
    Assert.assertEquals("Subtract result went wrong", result, 0);
  }

  @Test
  @DisplayName("Should multiply numbers")
  void multiplyIntegers() {
    Integer a = 5;
    Integer b = 5;
    Integer result = calculator.subtract(a, b);
    Assert.assertTrue(result == 0);
  }

  @Test
  @DisplayName("Should divide numbers")
  void divideIntegers() {
    Integer a = 5;
    Integer b = 5;
    int result = calculator.divide(a, b);
    Assert.assertTrue("Divide numbers went wrong", result == 1);
  }

  @Test
  @DisplayName("Should throw runtime npe exception")
  void multiplyByNullShouldThrowException() {
    Integer a = 5;
    Integer b = null;
    Assert.assertThrows(RuntimeException.class, () -> calculator.divide(a, b));
  }

  @Test
  @DisplayName("Should throw runtime exception")
  void divideIntegersShouldThrowRuntimeException() {
    Integer a = 5;
    Integer b = 0;
    Assert.assertThrows("No exception was thrown", RuntimeException.class, () -> calculator.divide(a, b));
  }

  @Test
  @DisplayName("Should throw npe")
  void addIntegersNPE() {
    Integer a = 5;
    Integer b = null;
    Assert.assertThrows(RuntimeException.class, () -> calculator.add(a, b));
  }

  @Test
  @DisplayName("Should throw npe")
  void subtractIntegersNPE() {
    Integer a = null;
    Integer b = 5;
    Assert.assertThrows(RuntimeException.class, () -> calculator.subtract(a, b));
  }

  @Test
  @DisplayName("Should throw npe")
  void multiplyIntegersNPE() {
    Integer a = null;
    Integer b = null;
    Assert.assertThrows(RuntimeException.class, () -> calculator.subtract(a, b));
  }

  @Test
  @DisplayName("Should throw npe")
  void divideIntegersNPE() {
    Integer a = null;
    Integer b = 5;
    Assert.assertThrows(RuntimeException.class, () -> calculator.divide(a, b));
  }
}