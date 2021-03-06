# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeJobsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'DescribeJobs','hbr')
		self.set_protocol_type('https')

	def get_JobId(self):
		return self.get_query_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_query_param('JobId',JobId)

	def get_ClientId(self):
		return self.get_query_params().get('ClientId')

	def set_ClientId(self,ClientId):
		self.add_query_param('ClientId',ClientId)

	def get_PolicyId(self):
		return self.get_query_params().get('PolicyId')

	def set_PolicyId(self,PolicyId):
		self.add_query_param('PolicyId',PolicyId)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_JobStatus(self):
		return self.get_query_params().get('JobStatus')

	def set_JobStatus(self,JobStatus):
		self.add_query_param('JobStatus',JobStatus)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_UserAccountId(self):
		return self.get_query_params().get('UserAccountId')

	def set_UserAccountId(self,UserAccountId):
		self.add_query_param('UserAccountId',UserAccountId)

	def get_JobType(self):
		return self.get_query_params().get('JobType')

	def set_JobType(self,JobType):
		self.add_query_param('JobType',JobType)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)