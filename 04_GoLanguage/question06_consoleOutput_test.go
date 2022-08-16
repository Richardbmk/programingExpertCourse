// This suite of tests is written to run against your code
// so that we can check its correctness.

package main

import (
	"github.com/stretchr/testify/require"
)

func (s *TestSuite) TestCase1(t *TestCase) {
	expected := "%27.2:true/hello"
	output := Format(27.2, true, "hello")
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase2(t *TestCase) {
	expected := "%-92.1:false/"
	output := Format(-92.1, false, "")
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase3(t *TestCase) {
	expected := "%32.987:true/TiM"
	output := Format(32.987, true, "TiM")
	require.Equal(t, expected, output)
}
