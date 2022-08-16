// This suite of tests is written to run against your code
// so that we can check its correctness.

package main

import (
	"github.com/stretchr/testify/require"
)

func (s *TestSuite) TestCase1(t *TestCase) {
	expected := 1
	output := Factorial(1)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase2(t *TestCase) {
	expected := 2
	output := Factorial(2)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase3(t *TestCase) {
	expected := 6
	output := Factorial(3)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase4(t *TestCase) {
	expected := 24
	output := Factorial(4)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase5(t *TestCase) {
	expected := 120
	output := Factorial(5)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase6(t *TestCase) {
	expected := 720
	output := Factorial(6)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase7(t *TestCase) {
	expected := 5040
	output := Factorial(7)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase8(t *TestCase) {
	expected := 40320
	output := Factorial(8)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase9(t *TestCase) {
	expected := 362880
	output := Factorial(9)
	require.Equal(t, expected, output)
}
