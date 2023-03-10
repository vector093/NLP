# -*- coding: utf-8 -*-
"""A3_2.5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sSXfhtY2tjjUydy4ULlruYxzNFJs1M_C
"""

def generate(self, idx, device, max_new_tokens, temperature=1.0, do_sample=False, top_k=None):
        """
        Take a conditioning sequence of indices idx (LongTensor of shape (b,t)) and complete
        the sequence max_new_tokens times, feeding the predictions back into the model each time.
        Most likely you'll want to make sure to be in model.eval() mode of operation for this.
        """
        prob=[]
        words=[]
        prob6_array=[]
        idx6_array=[]
        for _ in range(max_new_tokens):
            # if the sequence context is growing too long we must crop it at block_size
            idx_cond = idx if idx.size(1) <= self.block_size else idx[:, -self.block_size:]
            idx_cond.to(device)
            # forward the model to get the logits for the index in the sequence
            logits, _ = self(idx_cond)
            # pluck the logits at the final step and scale by desired temperature
            logits = logits[:, -1, :] / temperature
            # optionally crop the logits to only the top k options
            if top_k is not None:
                v, _ = torch.topk(logits, top_k)
                logits[logits < v[:, [-1]]] = -float('Inf')
            # apply softmax to convert logits to (normalized) probabilities
            probs = F.softmax(logits, dim=-1)
            # either sample from the distribution or take the most likely element
            if do_sample:
                idx_next = torch.multinomial(probs, num_samples=1)
            else:
                p, idx_next = torch.topk(probs, k=1, dim=-1)
                #print(p[0])
                prob.append(p[0])# single probs for each word
                words.append(idx_next)# predicted words
                prob6, idx6 = torch.topk(probs, k=6, dim=-1)
                prob6_array.append(prob6)# top 6 probs
                idx6_array.append(idx6)# top 6 words
            # append sampled index to the running sequence and continue
            idx = torch.cat((idx, idx_next), dim=1)
            
            
            #p=torch.cat((p,probs[0]))

        return idx,prob,idx6_array,prob6_array,words