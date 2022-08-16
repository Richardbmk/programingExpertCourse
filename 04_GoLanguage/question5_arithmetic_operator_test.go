// This suite of tests is written to run against your code
// so that we can check its correctness.

package main

import (
	"github.com/stretchr/testify/require"
)

func (s *TestSuite) TestCase1(t *TestCase) {
	var expected float64 = 3
	output := RoundedSquareRoot(10)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase2(t *TestCase) {
	var expected float64 = 4
	output := RoundedSquareRoot(14)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase3(t *TestCase) {
	var expected float64 = 10
	output := RoundedSquareRoot(100)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase4(t *TestCase) {
	var expected float64 = 11
	output := RoundedSquareRoot(122)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase5(t *TestCase) {
	var expected float64 = 0
	output := RoundedSquareRoot(0)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase6(t *TestCase) {
	var expected float64 = 8
	output := RoundedSquareRoot(64.23)
	require.Equal(t, expected, output)
}
