"""Fail-closed comparative derivative controls; standard-library only."""
import unittest
from rgc_score import remainder_derivative, run


class ComparisonEvidenceTests(unittest.TestCase):
    def test_missing_named_coefficient_cannot_confirm_outrunning(self):
        result = remainder_derivative("floor_only", 0.8, None, named_alpha_published=False)
        self.assertEqual(result["mode"], "remainder_floor_only")
        self.assertIsNone(result["rgc_holds"])
        self.assertIsNone(result["alpha_gap"])
        self.assertFalse(result["queued_false_saturation"])

    def test_unpublished_named_coefficient_is_hypothesis_only(self):
        result = remainder_derivative("scenario", 0.8, 0, named_alpha_published=False)
        self.assertEqual(result["mode"], "unverified_comparison")
        self.assertIsNone(result["rgc_holds"])
        self.assertTrue(result["hypothetical_false_saturation"])
        self.assertFalse(result["queued_false_saturation"])

    def test_published_outpacing_can_be_confirmed(self):
        result = remainder_derivative("paired", 0.8, 0.2, named_alpha_published=True)
        self.assertEqual(result["mode"], "remainder_outruns")
        self.assertIs(result["rgc_holds"], True)

    def test_published_same_rate_refuses_outrunning(self):
        result = remainder_derivative("matched", 0.2, 0.2, named_alpha_published=True)
        self.assertIs(result["rgc_holds"], False)

    def test_saturated_remainder_still_kills(self):
        result = remainder_derivative("saturated", 0, None, named_alpha_published=False)
        self.assertIs(result["rgc_holds"], False)
        self.assertTrue(result["kill_rule_fired"])

    def test_missing_published_coefficient_is_invalid(self):
        with self.assertRaisesRegex(ValueError, "named_alpha_published"):
            remainder_derivative("invalid", 0.7, None, named_alpha_published=True)

    def test_full_research_packet_no_longer_promotes_an_unverified_pair(self):
        result = run()
        by_id = {row["id"]: row for row in result["derivatives"]}
        self.assertIsNone(by_id["unbinned_vs_mag_floor"]["rgc_holds"])
        self.assertIsNone(by_id["false_saturation_queue"]["rgc_holds"])
        self.assertTrue(by_id["false_saturation_queue"]["hypothetical_false_saturation"])
        self.assertFalse(by_id["false_saturation_queue"]["queued_false_saturation"])


if __name__ == "__main__":
    unittest.main()
