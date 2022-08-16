// This suite of tests is written to run against your code
// so that we can check its correctness.

package main

import (
	"github.com/stretchr/testify/require"
)

func (s *TestSuite) TestCase1(t *TestCase) {
	expected := false
	output := XOR(false, false)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase2(t *TestCase) {
	expected := true
	output := XOR(false, true)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase3(t *TestCase) {
	expected := true
	output := XOR(true, false)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase4(t *TestCase) {
	expected := false
	output := XOR(true, true)
	require.Equal(t, expected, output)
}
