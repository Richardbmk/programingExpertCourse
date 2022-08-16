// This suite of tests is written to run against your code
// so that we can check its correctness.

package main

import (
	"github.com/stretchr/testify/require"
)

func (s *TestSuite) TestCase1(t *TestCase) {
	expected := 110
	output := MultiplyByString("22", 5)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase2(t *TestCase) {
	expected := 0
	output := MultiplyByString("0", 100)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase3(t *TestCase) {
	expected := 27
	output := MultiplyByString("-9", -3)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase4(t *TestCase) {
	expected := 0
	output := MultiplyByString("10", 0)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase5(t *TestCase) {
	expected := 132
	output := MultiplyByString("11", 12)
	require.Equal(t, expected, output)
}
