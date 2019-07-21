// Copyright 2019 Parity Technologies (UK) Ltd.
// This file is part of Substrate.

// Substrate is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// Substrate is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with Substrate.  If not, see <http://www.gnu.org/licenses/>.

//! The runtime api for building transactions.

use sr_api_macros::decl_runtime_apis;
use runtime_primitives::KeyTypeId;
use rstd::vec::Vec;

decl_runtime_apis! {
	/// The `TransactionBuilder` trait that provides required functions
	/// for building a transaction from a Call for the runtime.
	pub trait TransactionBuilder {
		/// Construct the payload.
		fn signing_payload(encoded_call: Vec<u8>, encoded_account_id: Vec<u8>) -> Vec<u8>;
		/// Build the transaction.
		fn build_transaction(signing_payload: Vec<u8>, encoded_account_id: Vec<u8>, signature: Vec<u8>) -> Vec<u8>;
		/// Get list of supported crypto types.
		fn possible_crypto() -> Vec<KeyTypeId>;
	}
}
